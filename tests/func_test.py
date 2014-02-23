#encoding: utf-8
import os
import sys
import copy
import json
import pprint
import random
import urlparse
import datetime

import func_test_constants as constants
sys.path.append('../lib')
import tools

CONFIG_PATH = '/usr/local/etc/test.conf'
settings = tools.Configuration(CONFIG_PATH).get_section('func_test')

class TestError(object):
    message_for_code = {
        1: 'Error on HTTP request',
        2: 'Unexpected response'
    }
    def __init__(self, code):
        self.code = code
        self.message = self.message_for_code[self.code]
        self.err_info = {}

    def save_and_exit(self, exit=True):
        print 'EXIT!'
        if exit:
            sys.exit(0)        

class Actor(object):
    # 0 - OK
    # 1 - error
    # 2 - response != expected_response
    def __init__(self, student_name):
        self.url_prefix = urlparse.urljoin(settings['url'], student_name)
        self.ok_response = {'message': 'OK', 'code': 0}

    def query_api(self, url_suffix, query_dict, post=False):
        url = self.url_prefix + '/' + url_suffix + '/'
        try:
            response = tools.Request(url, query_dict, post).get_response()
        except ValueError, e:
            err = TestError(1)
            err.info = {
                'url': url,
                'query_params': query_dict, 
                'response': str(e)
            }
            err.save_and_exit()

        return response

    def _create_from_dict(self, response, new_type=None):
        cls_for_location = {
            'forum': Forum,
            'thread': Thread,
            'post': Post,
            'user': User,
        }
        if new_type is None:
            for loc in cls_for_location:
                if loc in self.url_prefix:
                    cls = cls_for_location[loc]
        else:
            cls = cls_for_location[new_type]

        return cls(**response)

    def _trigger_side_effects(self, test_obj):
        TestScenario.add(test_obj)
        if test_obj.type == 'post':
            thread = TestScenario.get_obj(obj_type='thread', obj_id=test_obj.thread)
            thread.posts += 1

    def create(self, query_dict):
        related_for_type = {
            'thread': ['forum', 'user'],
            'user': [],
            'forum': [],
            'post': ['thread', 'forum', 'user'],
        }
        url_suffix = 'create'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        api_obj = self._create_from_dict(response)        
        test_obj = self._create_from_dict(query_dict)        
        test_obj.id = api_obj.id
        self._trigger_side_effects(test_obj)
        self.validate_single(test_obj, related=related_for_type[test_obj.type])
        return test_obj

    def details(self, obj, related):
        url_suffix = 'details'
        query_dict = {
            obj.type: obj.unique_id,
            'related': related,
        }

        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)
        obj = self._create_from_dict(response)        
        return obj

    def validate_single(self, test_obj, related=None):
        if related is None:
            related = []
        api_obj = self.details(obj=test_obj, related=related)
        if test_obj != api_obj:
            print 'single: ', False
            return False
        print 'single: ', True
        return True

    def validate_list(self, test_obj_list, api_obj_list):
        # print 'GOT: api=', api_obj_list, 'test=', test_obj_list
        if len(api_obj_list) == len(test_obj_list):
            for test_obj, api_obj in zip(test_obj_list, api_obj_list):
                if test_obj != api_obj:
                    # print test_obj
                    # print api_obj
                    print 'Objs dont match.list: ', False
                    return False
        else:
            print api_obj_list, test_obj_list
            print 'Len dont match.list: ', False
            return False
        print 'list: ', True
        return True



class ForumActor(Actor):
    def __init__(self, student_name):
        super(ForumActor, self).__init__(student_name)
        self.url_prefix = self.url_prefix + '/forum'

    def list_type(self, obj_type, query_dict, validate_against):
        url_suffix = 'list' + obj_type.capitalize() + 's'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)['response']
        api_obj_list = [self._create_from_dict(obj_dict, new_type=obj_type) for obj_dict in response]
        return self.validate_list(validate_against, api_obj_list)


class ThreadActor(Actor):
    def __init__(self, student_name):
        super(ThreadActor, self).__init__(student_name)
        self.url_prefix = self.url_prefix + '/thread'

    def list(self, query_dict, validate_against):
        url_suffix = 'list'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)['response']
        api_obj_list = [self._create_from_dict(obj_dict) for obj_dict in response]
        return self.validate_list(validate_against, api_obj_list)

    def open(self, query_dict, thread):
        thread.isClosed = False
        url_suffix = 'open'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(thread)

    def close(self, query_dict, thread):
        thread.isClosed = True
        url_suffix = 'close'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(thread)

    def remove(self, query_dict, thread):
        thread.isDeleted = True
        url_suffix = 'remove'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(thread)

    def restore(self, query_dict, thread):
        thread.isDeleted = False
        url_suffix = 'restore'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(thread)

    def subscribe(self, query_dict, thread):
        user = TestScenario.get_obj(obj_type='user', obj_id=query_dict['user'])
        if thread.unique_id not in user.subscriptions:
            user.subscriptions.append(thread.unique_id)
        url_suffix = 'subscribe'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(thread)

    def unsubscribe(self, query_dict, thread):
        user = TestScenario.get_obj(obj_type='user', obj_id=query_dict['user'])
        if thread.unique_id in user.subscriptions:
            user.subscriptions.remove(thread.unique_id)
        url_suffix = 'unsubscribe'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(thread)

    def update(self, query_dict, thread):
        thread.message = query_dict['message']
        thread.slug = query_dict['slug']
        url_suffix = 'update'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(thread)

    def vote(self, query_dict, thread):
        v = query_dict['vote']
        if v == 1: thread.likes += 1
        if v == -1: thread.dislikes += 1
        thread.points += v
        url_suffix = 'vote'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(thread)


class PostActor(Actor):
    def __init__(self, student_name):
        super(PostActor, self).__init__(student_name)
        self.url_prefix = self.url_prefix + '/post'

    def list(self, query_dict, validate_against):
        url_suffix = 'list'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)['response']
        api_obj_list = [self._create_from_dict(obj_dict) for obj_dict in response]
        return self.validate_list(validate_against, api_obj_list)

    def remove(self, query_dict, post):
        post.isDeleted = True
        url_suffix = 'remove'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(post)

    def restore(self, query_dict, post):
        post.isDeleted = False
        url_suffix = 'restore'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(post)

    def update(self, query_dict, post):
        post.message = query_dict['message']
        url_suffix = 'update'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(post)

    def vote(self, query_dict, post):
        v = query_dict['vote']
        if v == 1: post.likes += 1
        if v == -1: post.dislikes += 1
        post.points += v
        url_suffix = 'vote'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(post)

class UserActor(Actor):
    def __init__(self, student_name):
        super(UserActor, self).__init__(student_name)
        self.url_prefix = self.url_prefix + '/user'


class ForumEntity(object):
    def __init__(self, **kwargs):
        for a, v in kwargs.items():
            setattr(self, a, v)    

    def __str__(self):
        return pprint.pformat(self.__dict__)

    @property
    def type(self):
        return self.__class__.__name__.lower()

    @property
    def unique_id(self):
        id_attr_for_type = {
            'forum': 'short_name',
            'thread': 'id',
            'post': 'id',
            'user': 'email',
        }
        cls = self.type
        id_attr = id_attr_for_type[cls]
        return getattr(self, id_attr)

    def __cmp__(self, obj):
        cls_for_attr = {
            'forum': Forum,
            'thread': Thread,
            'user': User,
        }
        if obj:
            to_dict = self.__dict__
            ao_dict = obj.__dict__

            for attr in to_dict:
                if attr in ao_dict:
                    if isinstance(ao_dict[attr], dict) or isinstance(to_dict[attr], dict):
                        if not isinstance(ao_dict[attr], dict):
                            print 'No related supplied'
                            return -1
                        cls = cls_for_attr[attr]
                        related_ao = cls(**ao_dict[attr])
                        ao_dict[attr] = related_ao.unique_id
                        if isinstance(to_dict[attr], dict):
                            cls = cls_for_attr[attr]
                            related_to = cls(**to_dict[attr])
                            to_dict[attr] = related_to.unique_id
                        if isinstance(to_dict[attr], (str, unicode, int)):
                            related_to = TestScenario.get_eq_obj(related_ao)
                        if related_to != related_ao:
                            print 'Related %s do not match' % attr
                            return -1
                    if to_dict[attr] != ao_dict[attr]:
                        print '%s do not match: api=%s, test=%s' % (attr, str(ao_dict[attr]) , str(to_dict[attr]))
                        return -1
                else:
                    print 'Missing attr: %s' % attr
                    return -1
            else:
                return 0
        print 'No api obj'
        return -1

class Forum(ForumEntity):
    pass

class Thread(ForumEntity):
    def __init__(self, **kwargs):
        self.dislikes = 0
        self.likes = 0
        self.posts = 0
        self.points = 0
        super(Thread, self).__init__(**kwargs)

class Post(ForumEntity):
    def __init__(self, **kwargs):
        self.parent = None
        self.points = 0
        self.dislikes = 0
        self.likes = 0
        super(Post, self).__init__(**kwargs)

class User(ForumEntity):
    def __init__(self, **kwargs):
        self.isFollowing = False
        self.isFollowedBy = False
        self.subscriptions = []
        super(User, self).__init__(**kwargs)


class EntitiesList(object):
    def __init__(self, objects, **kwargs):
        self.objects = objects
        if 'since' in kwargs:
            self.filter_since(kwargs['since'])
        for attr in ('forum', 'thread', 'user'):
            if attr in kwargs:
                self.filter_by_attr(attr, kwargs[attr])
        if 'since_id' in kwargs:
            self.filter_since_id(kwargs['since_id'])
        if 'related' in kwargs:
            self.include_related(kwargs['related'])
        if 'order' in kwargs:
            self.order_by(kwargs['order'])
        else:
            self.order_by()
        if 'limit' in kwargs:
            self.limit(kwargs['limit'])

    def filter_by_attr(self, attr, value):
        objects = self.objects[:]
        self.objects = []
        for obj in objects:
            obj_value = getattr(obj, attr)
            if isinstance(obj_value, int) and isinstance(value, (str, unicode)):
                test_obj = TestScenario.get_obj(obj_type=attr, obj_id=obj_value)
                if attr in ('forum'):
                    obj_value = test_obj.short_name
                if attr in ('thread'):
                    obj_value = test_obj.slug
                if attr in ('user'):
                    obj_value = test_obj.email
            if obj_value == value:
                self.objects.append(obj)

    def filter_since(self, date):
        get_datetime = lambda date_str: datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        objects = self.objects[:]
        self.objects = []
        since_date = get_datetime(date)
        for obj in objects:
            obj_date = get_datetime(obj.date)
            if obj_date >= since_date:
                self.objects.append(obj)

    def filter_since_id(self, since_id):
        objects = self.objects[:]
        self.objects = []
        for obj in objects:
            if obj.id >= since_id:
                self.objects.append(obj)

    def include_related(self, related):
        for obj in self.objects:
            for r in related:
                r_id = getattr(obj, r)
                r_obj = TestScenario.get_obj(obj_type=r, obj_id=r_id)
                setattr(obj, r, r_obj.__dict__)

    def order_by(self, order='desc'):
        if self.objects:
            order = True if order == 'desc' else False
            if hasattr(self.objects[0], 'date'):
                get_datetime = lambda obj: datetime.datetime.strptime(obj.date, '%Y-%m-%d %H:%M:%S')
                self.objects.sort(key=get_datetime, reverse=order)
            else:
                self.objects.sort(key=lambda obj: obj.id, reverse=order)


    def limit(self, limit_by):
        self.objects = self.objects[:limit_by]


class TestScenario(object):
    forums = {}
    posts = {}
    threads = {}
    users = {}
    container_for_type = {
        'forum': forums,
        'thread': threads,
        'post': posts,
        'user': users,
    }

    @staticmethod
    def add(obj):
        container = TestScenario.container_for_type[obj.type]
        container[obj.unique_id] = obj

    @staticmethod
    def get_eq_obj(obj):
        container = TestScenario.container_for_type[obj.type]
        return container[obj.unique_id]

    @staticmethod
    def get_obj(obj_id, obj_type):
        container = TestScenario.container_for_type[obj_type]
        return container[obj_id]

    def __init__(self, student_name):
        self.forum_actor = ForumActor(student_name)
        self.post_actor = PostActor(student_name)
        self.thread_actor = ThreadActor(student_name)
        self.user_actor = UserActor(student_name)
        self.test_conf = constants.TEST_CONF

    def start(self):
        self.register_users()
        self.create_content()
        self.test_forums()
        self.test_posts()
        self.test_threads()

    def register_users(self):
        for u in self.test_conf['users']:
            self.user_actor.create(u)

    def create_content(self):
        for f in self.test_conf['forums']:
            f['user'] = random.choice(self.users.keys())
            self.forum_actor.create(f)

        for t in self.test_conf['threads']:
            t['forum'] = random.choice(self.forums.keys())
            t['user'] = random.choice(self.users.keys())
            thread = self.thread_actor.create(t)

        self._setup_posts_tree(self.test_conf['posts'])

    # DFS tree construction
    def _setup_posts_tree(self, posts, parent=None, thread_id=None):
        for p in posts:
            childs = []
            if 'childs' in p:
                childs = p['childs']
                del p['childs']
            if parent is not None:
                p['parent'] = parent
                p['thread'] = thread_id
            else:
                p['thread'] = random.choice(self.threads.keys())
            thread = self.threads[p['thread']]
            p['forum'] = thread.forum
            p['user'] = random.choice(self.users.keys())
            created_post = self.post_actor.create(p)
            if childs: self._setup_posts_tree(childs, parent=created_post.id, thread_id=p['thread'])

    def test_forums(self):
        for params in constants.TEST_FORUMS['listPosts']:
            objects = copy.deepcopy(self.posts.values())
            elist = EntitiesList(objects, **params)
            if not self.forum_actor.list_type('post', params, elist.objects):
                break
        
        for params in constants.TEST_FORUMS['listThreads']:
            objects = copy.deepcopy(self.threads.values()) 
            elist = EntitiesList(objects, **params)
            if not self.forum_actor.list_type('thread', params, elist.objects):
                break
        
        for params in constants.TEST_FORUMS['listUsers']:
            objects = []
            for p in self.posts.values():
                user = self.users[p.user]
                forum = self.forums[p.forum]
                if forum.short_name == params['forum']:
                    objects.append(user)
            params_cp = copy.deepcopy(params)
            del params_cp['forum']
            elist = EntitiesList(objects, **params_cp)
            self.forum_actor.list_type('user', params, elist.objects)

    def test_posts(self):
        for params in constants.TEST_POSTS['list']:
            objects = copy.deepcopy(self.posts.values()) 
            elist = EntitiesList(objects, **params)
            self.post_actor.list(params, elist.objects)
        
        post = random.choice(self.posts.values())
        self.post_actor.remove({'post': post.id}, post)
        self.post_actor.restore({'post': post.id}, post)
        self.post_actor.update({'post': post.id, 'message': post.message}, post)
        for _ in range(constants.TEST_POSTS['votes']):
            post = random.choice(self.posts.values())
            vote = random.choice([1, -1])
            self.post_actor.vote({'post': post.id, 'vote': vote}, post)

    def test_threads(self):
        for params in constants.TEST_THREADS['list']:
            objects = copy.deepcopy(self.threads.values()) 
            elist = EntitiesList(objects, **params)
            self.thread_actor.list(params, elist.objects)
        
        thread = random.choice(self.threads.values())
        self.thread_actor.remove({'thread': thread.id}, thread)
        self.thread_actor.restore({'thread': thread.id}, thread)
        self.thread_actor.close({'thread': thread.id}, thread)
        self.thread_actor.open({'thread': thread.id}, thread)
        self.thread_actor.update({'thread': thread.id, 'message': thread.message, 'slug': 'newslug'}, thread)
        for _ in range(constants.TEST_THREADS['votes']):
            thread = random.choice(self.threads.values())
            vote = random.choice([1, -1])
            self.thread_actor.vote({'thread': thread.id, 'vote': vote}, thread)
        for _ in range(constants.TEST_THREADS['subscriptions']):
            thread = random.choice(self.threads.values())
            user = random.choice(self.users.values())
            self.thread_actor.subscribe({'thread': thread.id, 'user': user.unique_id}, thread)
        for _ in range(constants.TEST_THREADS['unsubscriptions']):
            thread = random.choice(self.threads.values())
            user = random.choice(self.users.values())
            self.thread_actor.unsubscribe({'thread': thread.id, 'user': user.unique_id}, thread)

if __name__ == '__main__':
    pass
    TestScenario(student_name='s.stupnikov').start()