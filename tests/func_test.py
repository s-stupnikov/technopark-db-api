#encoding: utf-8
import os
import sys
import copy
import json
import time
import pprint
import random
import requests
import urlparse
import datetime
import itertools
from optparse import OptionParser

import func_test_constants as constants
sys.path.append('../lib')
sys.path.append('../doc')

import tools
from doc_conf import DISCR

CONFIG_PATH = '/usr/local/etc/test.conf'
settings = tools.Configuration(CONFIG_PATH).get_section('func_test')

class TestLog(object):
    def __init__(self, verbose=False):
        self.test_log = []
        self.verbose = verbose

    def write(self, message, level='info'):
        time = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')
        msg = time + message
        if self.verbose:
            print message
        self.test_log.append({'message': message, 'level': level})


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


docs = {}
log = None
class Actor(object):
    # 0 - OK
    # 1 - error
    # 2 - response != expected_response
    def __init__(self, student_ip):
        self.url_prefix = settings['url'].replace('ip', student_ip)
        self.ok_response = {'message': 'OK', 'code': 0}

    def query_api(self, url_suffix, query_dict, post=False):
        url = self.url_prefix + '/' + url_suffix + '/'
        if 'details' not  in url_suffix:
            self.url_suffix = url_suffix
        method = 'POST' if post else 'GET'
        log.write('Requesting %s with %s (%s)' % (url, repr(query_dict), method))
        try:
            start = time.time()
            response = tools.Request(url, query_dict, post).get_response()
            self.doc(url, query_dict, method, response)
            req_time = time.time() - start
            log.write('Request time was: %.4f sec' % req_time)
        except ValueError, e:
            log.write('Request error: %s' % str(e), level='error')
            location = self.url_prefix.split('/')[-1] + '/' + url_suffix
            if 'details' not in location:
                TESTS[location] = False
            # log.write('Exiting', level='error')
            # raise ValueError
            response = {}
        return response

    def doc(self, url, query_dict, method, response):
        optional_args = set(['order', 'since', 'since_id', 'limit', 'related', 'isAnonymous', 'isApproved', 'isSpam', 'isDeleted', 'isEdited', 'isHighlighted', 'parent'])
        get_arg_type = lambda k: 'optional' if k in optional_args else 'requried'
        path_parts = url.split('api')[1].strip('/').split('/')
        entity_name = path_parts[0]
        entity_method = path_parts[1]
        path = os.path.join('../doc', entity_name, entity_method + '.md')
        response = {u'code': 0, u'response': response}
        if method == 'GET':
            url = requests.Request("GET", url.replace('127.0.0.1:5000', 'some.host.ru'), params=query_dict).prepare().url
        else:
            url = url.replace('127.0.0.1:5000', 'some.host.ru')
        context = {
            'entity_name': entity_name,
            'entity_method': entity_method,
            'method': method,
            'requried': set(),
            'optional': set(),
            'formats': "\n##Supported formats\n* json\n" if method == "POST" else '',
            'response': json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')),
            'url': url,
            'params': ' with *%s*' % json.dumps(query_dict) if method == "POST" else '',
        }
        for k in query_dict:
            context[get_arg_type(k)].add(k)

        if path not in docs:
            docs[path] = context
        else:
            for p in context['optional']: docs[path]['optional'].add(p)
            for p in context['requried']: docs[path]['requried'].add(p)
            # docs[path]['requried'] &= context['requried']
            if '[]' in docs[path]['response'] and response['response']:
                docs[path]['url'] = context['url']
                docs[path]['response'] = context['response']
                docs[path]['params'] = context['params']

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
        try:
            obj = cls(**response)
        except Exception, e:
            log.write('Cannot create <%s> object from response. Response: %s' % (cls.__name__, str(response)), level='error')
            obj = cls()
        return obj

    def _trigger_side_effects(self, test_obj):
        TestScenario.add(test_obj)
        if test_obj.type == 'post':
            thread = TestScenario.get_obj(obj_type='thread', obj_id=test_obj.thread)
            thread.posts += 1

    def create(self, query_dict, plain=False):
        related_for_type = {
            'thread': ['forum', 'user'],
            'forum': ['user'],
            'post': ['thread', 'forum', 'user'],
        }
        url_suffix = 'create'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        if plain:
            return response
        api_obj = self._create_from_dict(response)        
        test_obj = self._create_from_dict(query_dict)
        test_obj.id = api_obj.id if hasattr(api_obj, 'id') else -1
        self._trigger_side_effects(test_obj)
        self.validate_single(test_obj, related=related_for_type.get(test_obj.type))
        return test_obj

    def details(self, obj, related, plain=False):
        url_suffix = 'details'
        query_dict = {
            obj.type: obj.unique_id,
        }
        if related: query_dict['related'] = related

        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)
        if plain:
            return response
        obj = self._create_from_dict(response)        
        return obj

    def _get_api_location(self):
        return self.url_prefix.split('/')[-1] + '/' + self.url_suffix

    def validate_single(self, test_obj, related=None, only_check=False):
        location = self._get_api_location()
        log.write('Validating by requesting object details')
        if related is None:
            related = []
        api_obj = self.details(obj=test_obj, related=related)
        try:
            is_valid = test_obj == api_obj
        except Exception, e:
            log.write('Validation error: %s' % e, level='error')
            is_valid = False
        if (location not in TESTS or TESTS.get(location) != False) and not only_check:
            TESTS[location] = is_valid
        return is_valid

    def validate_list(self, test_obj_list, api_obj_list):
        location = self._get_api_location()
        log.write('Validating by requesting list of objects')
        if len(api_obj_list) == len(test_obj_list):
            for test_obj, api_obj in itertools.izip_longest(test_obj_list, api_obj_list):
                try:
                    if test_obj != api_obj:
                        TESTS[location] = False
                        log.write('obj {} != obj {}'.format(test_obj, api_obj))
                except Exception, e:
                    log.write('Validation error: %s' % e, level='error')
                    TESTS[location] = False
        else:
            TESTS[location] = False
            log.write('len(api objects list) != len(test object list): %d != %d' % (len(api_obj_list), len(test_obj_list)), level='error')
        if TESTS.get(location, True):
            TESTS[location] = True
        return TESTS.get(location)


class ForumActor(Actor):
    def __init__(self, student_ip):
        super(ForumActor, self).__init__(student_ip)
        self.url_prefix = self.url_prefix + '/forum'

    def list_type(self, obj_type, query_dict, validate_against):
        url_suffix = 'list' + obj_type.capitalize() + 's'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)
        api_obj_list = [self._create_from_dict(obj_dict, new_type=obj_type) for obj_dict in response]
        return self.validate_list(validate_against, api_obj_list)


class ThreadActor(Actor):
    def __init__(self, student_ip):
        super(ThreadActor, self).__init__(student_ip)
        self.url_prefix = self.url_prefix + '/thread'

    def list(self, query_dict, validate_against):
        url_suffix = 'list'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)
        api_obj_list = [self._create_from_dict(obj_dict) for obj_dict in response]
        return self.validate_list(validate_against, api_obj_list)

    def list_posts(self, query_dict, validate_against): 
        url_suffix = 'listPosts'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)
        api_obj_list = [self._create_from_dict(obj_dict, new_type='post') for obj_dict in response]
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

    def remove(self, query_dict, thread, thread_posts):
        thread.isDeleted = True
        for p in thread_posts:
            p.isDeleted = True
            thread.posts -= 1
        url_suffix = 'remove'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        is_thread_valid = self.validate_single(thread)
        location = self._get_api_location()
        list_posts_validity = TESTS.get('thread/listPosts')
        query_dict['order'] = 'desc'
        TESTS[location] = self.list_posts(query_dict, thread_posts) and is_thread_valid
        TESTS['thread/listPosts'] = True if list_posts_validity else False
        return TESTS[location]

    def restore(self, query_dict, thread, thread_posts):
        thread.isDeleted = False
        for p in thread_posts:
            p.isDeleted = False
            thread.posts += 1
        url_suffix = 'restore'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        is_thread_valid = self.validate_single(thread)
        location = self._get_api_location()
        list_posts_validity = TESTS.get('thread/listPosts')
        query_dict['order'] = 'desc'
        TESTS[location] = self.list_posts(query_dict, thread_posts) and is_thread_valid
        TESTS['thread/listPosts'] = True if list_posts_validity else False
        return TESTS[location]

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
    def __init__(self, student_ip):
        super(PostActor, self).__init__(student_ip)
        self.url_prefix = self.url_prefix + '/post'

    def list(self, query_dict, validate_against):
        url_suffix = 'list'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)
        api_obj_list = [self._create_from_dict(obj_dict) for obj_dict in response]
        return self.validate_list(validate_against, api_obj_list)

    def remove(self, query_dict, post):
        post.isDeleted = True
        thread = TestScenario.threads[post.thread]
        thread.posts -= 1
        url_suffix = 'remove'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        is_post_valid = self.validate_single(post)
        location = self._get_api_location()
        TESTS[location] = testsuite.thread_actor.validate_single(thread, only_check=True) and is_post_valid
        return TESTS[location]

    def restore(self, query_dict, post):
        post.isDeleted = False
        thread = TestScenario.threads[post.thread]
        thread.posts += 1
        url_suffix = 'restore'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        is_post_valid = self.validate_single(post)
        location = self._get_api_location()
        TESTS[location] = testsuite.thread_actor.validate_single(thread, only_check=True) and is_post_valid
        return TESTS[location]

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
    def __init__(self, student_ip):
        super(UserActor, self).__init__(student_ip)
        self.url_prefix = self.url_prefix + '/user'

    def update_profile(self, query_dict, user):
        user.name = query_dict['name']
        user.about = query_dict['about']
        url_suffix = 'updateProfile'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        return self.validate_single(user)

    def list_posts(self, query_dict, validate_against):
        url_suffix = 'listPosts'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)
        api_obj_list = [self._create_from_dict(obj_dict, new_type='post') for obj_dict in response]
        return self.validate_list(validate_against, api_obj_list)

    def list_followers(self, query_dict, validate_against):
        url_suffix = 'listFollowers'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)
        api_obj_list = [self._create_from_dict(obj_dict) for obj_dict in response]
        return self.validate_list(validate_against, api_obj_list)

    def list_following(self, query_dict, validate_against):
        url_suffix = 'listFollowing'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict)
        api_obj_list = [self._create_from_dict(obj_dict) for obj_dict in response]
        return self.validate_list(validate_against, api_obj_list)

    def follow(self, query_dict, follower, followee):
        if followee.unique_id not in follower.following:
            follower.following.append(followee.unique_id)
        if follower.unique_id not in followee.followers:
            followee.followers.append(follower.unique_id)
        url_suffix = 'follow'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        r1 = self.validate_single(follower)
        r2 = self.validate_single(followee)
        return r1 and r2

    def unfollow(self, query_dict, follower, followee):
        if followee.unique_id in follower.following:
            follower.following.remove(followee.unique_id)
        if follower.unique_id in followee.followers:
            followee.followers.remove(follower.unique_id)
        url_suffix = 'unfollow'
        response = self.query_api(url_suffix=url_suffix, query_dict=query_dict, post=True)
        r1 = self.validate_single(follower)
        r2 = self.validate_single(followee)
        return r1 and r2

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

    @property
    def sort_field(self):
        sort_field_for_type = {
            'thread': 'date',
            'post': 'date',
            'user': 'name',
        }
        cls = self.type
        field = sort_field_for_type[cls]
        return getattr(self, field)

    def __cmp__(self, obj):
        cls_for_attr = {
            'forum': Forum,
            'thread': Thread,
            'user': User,
        }
        if obj:
            to_dict = copy.deepcopy(self.__dict__)
            ao_dict = copy.deepcopy(obj.__dict__)

            for attr in to_dict:
                if attr in ao_dict:
                    if isinstance(ao_dict[attr], dict) or isinstance(to_dict[attr], dict):
                        if not isinstance(ao_dict[attr], dict):
                            log.write('No <%s> related in response from API: [%s]' % (attr, repr(ao_dict)), level='error')
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
                            log.write('Related <%s> from API response [%s] dont match test object [%s]' % (attr, repr(ao_dict.get(attr)), repr(to_dict[attr])), level='error')
                            return -1
                    if isinstance(to_dict[attr], (set,list)) and isinstance(ao_dict[attr], (set, list)):
                        to_dict[attr] = set(to_dict[attr])
                        ao_dict[attr] = set(ao_dict[attr])
                    if to_dict[attr] != ao_dict[attr]:
                        log.write('Attribute <%s> from API response (value=%s) dont match test object (value=%s)' % (attr, repr(ao_dict.get(attr)), repr(to_dict[attr])), level='error')
                        return -1
                else:
                    log.write('Attribute <%s> missing in response from API: %s' % (attr, repr(ao_dict.get(attr))), level='error')
                    return -1
            else:
                return 0
        log.write('API object is empty', level='error')
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
        self.followers = []
        self.following = []
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

        if 'sort' in kwargs and kwargs['sort'] != 'flat':
            self.sort(kwargs['sort'], kwargs.get('order', 'desc'), kwargs.get('limit'))
        else:
            self.order_by(kwargs.get('order', 'desc'))
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

    def order_by(self, order='desc', objects=None):
        objects = objects or self.objects
        if objects:
            order = True if order == 'desc' else False
            if hasattr(objects[0], 'date'):
                get_datetime = lambda obj: datetime.datetime.strptime(obj.date, '%Y-%m-%d %H:%M:%S')
                objects.sort(key=get_datetime, reverse=order)
            else:
                objects.sort(key=lambda obj: obj.sort_field, reverse=order)

    def limit(self, limit_by):
        self.objects = self.objects[:limit_by]

    def sort(self, sort, order, limit):
        def _flatten_tree(tree, arr): #TODO: beware circling
            for node in tree:
                arr.append(node)
                if hasattr(node, 'childs'):
                    childs = node.childs
                    _flatten_tree(childs, arr)
                    del node.childs
            return arr
        sorted_objects = []
        self.order_by(order="asc")
        posts = dict((post.unique_id, post) for post in self.objects)
        num_posts = 0
        for post in self.objects:
            if post.parent is None:
                sorted_objects.append(post)
            else:
                parent_post = posts[post.parent]
                if not hasattr(parent_post, 'childs'):
                    parent_post.childs = []
                parent_post.childs.append(post)
        self.order_by(order, sorted_objects)
        if sort == 'parent_tree':
            sorted_objects = _flatten_tree(sorted_objects[:limit], [])
        elif sort == 'tree':
            sorted_objects = _flatten_tree(sorted_objects, [])[:limit]
        self.objects = sorted_objects


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

    def __init__(self, student_ip):
        self.student_ip = student_ip
        TestScenario.forums.clear()
        TestScenario.posts.clear()
        TestScenario.threads.clear()
        TestScenario.users.clear()          

        self.forum_actor = ForumActor(student_ip)
        self.post_actor = PostActor(student_ip)
        self.thread_actor = ThreadActor(student_ip)
        self.user_actor = UserActor(student_ip)
        self.test_conf = constants.TEST_CONF

    def start(self):
        log.write('Clear all')
        try:
            tools.Request('http://%s/db/api/clear/' % self.student_ip, {}, post=True).get_response()
            TESTS["clear"] = True
        except Exception, e:
            log.write("/clear call error: %s" % e, level='error')
            TESTS["clear"] = False

        # run tests    
        self.register_users()
        self.create_content()
        self.test_errors()
        self.test_posts()
        self.test_threads()
        self.test_users()
        self.test_forums()

    def register_users(self):
        log.write('Let there be users.')
        for u in self.test_conf['users']:
            self.user_actor.create(u)

    def create_content(self):
        log.write('Let there be content')
        for f in self.test_conf['forums']:
            f['user'] = random.choice(self.users.keys())
            self.forum_actor.create(f)

        for t in self.test_conf['threads']:
            t['forum'] = random.choice(self.forums.keys())
            t['user'] = random.choice(self.users.keys())
            thread = self.thread_actor.create(t)
            self._create_posts(thread.id)

    def _create_posts(self, thread):
        def generate_random_string(index):
            return 'my message {}'.format(index) * random.randint(self.test_conf['min_post_content_length'], self.test_conf['max_post_content_length'])
            
        def generate_random_boolean():
            return random.random() > 0.5

        def generate_random_date(first_date):
            def date_to_timestamp(d) :
                return int(time.mktime(d.timetuple()))

            def randomDate(start, end):
                """Get a random date between two dates"""
                stime = date_to_timestamp(start)
                etime = date_to_timestamp(end)
                ptime = stime + 1 + random.random() * (etime - stime - 1)
                new_date = datetime.datetime.fromtimestamp(ptime)
                return new_date, new_date.strftime("%Y-%m-%d %H:%M:%S")
            return randomDate(first_date, datetime.datetime.now())

        def generate_random_parent_id_and_tid(posts, tread):
            is_child = random.random() > self.test_conf['single_posts_rate']
            post_indexes = [index for index in posts.keys() if posts[index].thread == thread.id]
            if (is_child and post_indexes):
                parent = posts[random.choice(post_indexes)] 
                return parent.id, parent.thread, parent.forum
            else:
                return None, thread.id, thread.forum

        posts_number = random.randint(self.test_conf['min_posts_number'], self.test_conf['max_posts_number'])
        first_date = datetime.datetime(2014, 1, 1, 0, 0,0)
        thread = self.threads.get(thread)
        for index in xrange(posts_number):
            first_date, date = generate_random_date(first_date)
            parent, thread_id, forum = generate_random_parent_id_and_tid(self.posts, thread)
            post = {
                'message': generate_random_string(index),
                'isApproved': generate_random_boolean(),
                'isSpam': generate_random_boolean(),
                'isDeleted': False,
                'isEdited': generate_random_boolean(),
                'isHighlighted': generate_random_boolean(),
                'date': date,
                'parent': parent,
                'thread': thread_id,
                'forum': forum,
                'user': random.choice(self.users.keys()),
            }
            self.post_actor.create(post)

           
    # DFS tree construction
    def _setup_posts_tree(self, parent=None, thread_id=None):
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

    def test_errors(self):
        post = random.choice(self.posts.values())
        not_found_post = copy.deepcopy(post)
        not_found_post.id = -42
        res = self.post_actor.details(not_found_post, related=[], plain=True)
        res = res if isinstance(res, dict) else {"code": 0, "response": res}
        if res.get("code") == 1:
            TESTS["errors"] = True
        else:
            TESTS["errors"] = False
            log.write("Get nonexisting post response code was %s instead %s" % (res.get("code"), 1), level='error')
        u = random.choice(self.test_conf['users'])
        res = self.user_actor.create(u, plain=True)
        res = res if isinstance(res, dict) else {"code": 0, "response": res}
        if res.get("code") == 5:
            TESTS["errors"] = TESTS["errors"] and True
        else:
            TESTS["errors"] = TESTS["errors"] and False
            log.write("Create existing user response code was %s instead %s" % (res.get("code"), 5), level='error')

        thread = random.choice(self.threads.values())
        res = self.thread_actor.details(thread, related=["user", "thread"], plain=True)
        res = res if isinstance(res, dict) else {"code": 0, "response": res}
        if res.get("code") == 3:
            TESTS["errors"] = TESTS["errors"] and True
        else:
            TESTS["errors"] = TESTS["errors"] and False
            log.write("Incorrect request response code was %s instead %s" % (res.get("code"), 3), level='error')


    def test_forums(self):
        # print 'TEST FORUMS'
        log.write('List forum posts')
        for params in constants.TEST_FORUMS['listPosts']:
            objects = copy.deepcopy(self.posts.values())
            elist = EntitiesList(objects, **params)
            if not self.forum_actor.list_type('post', params, elist.objects):
                break
        
        log.write('List forum threads')
        for params in constants.TEST_FORUMS['listThreads']:
            objects = copy.deepcopy(self.threads.values()) 
            elist = EntitiesList(objects, **params)
            if not self.forum_actor.list_type('thread', params, elist.objects):
                break
        
        log.write('List forum users')
        for params in constants.TEST_FORUMS['listUsers']:
            objects = []
            for p in self.posts.values():
                user = self.users[p.user]
                forum = self.forums[p.forum]
                if forum.short_name == params['forum']:
                    if user.id not in [u.id for u in objects]:
                        objects.append(user)
            params_cp = copy.deepcopy(params)
            del params_cp['forum']
            elist = EntitiesList(objects, **params_cp)
            self.forum_actor.list_type('user', params, elist.objects)

    def test_posts(self):
        # print 'TEST POSTS'
        log.write('List posts')
        for params in constants.TEST_POSTS['list']:
            objects = copy.deepcopy(self.posts.values())
            if 'forum' not in params:
                thread = random.choice(self.threads.values()) 
                params['thread'] = thread.id
            elist = EntitiesList(objects, **params)
            self.post_actor.list(params, elist.objects)
        
        post = random.chonot_found_post = random.choice(self.posts.values())
        log.write('Remove post')
        self.post_actor.remove({'post': post.id}, post)
        log.write('Restore post')
        self.post_actor.restore({'post': post.id}, post)
        log.write('Update post')
        self.post_actor.update({'post': post.id, 'message': post.message}, post)
        log.write('Likes time!!!')
        for _ in range(constants.TEST_POSTS['votes']):
            post = random.choice(self.posts.values())
            vote = random.choice([1, -1])
            self.post_actor.vote({'post': post.id, 'vote': vote}, post)

    def test_threads(self):
        # print 'TEST THREADS'
        log.write('List some threads')
        for params in constants.TEST_THREADS['list']:
            objects = copy.deepcopy(self.threads.values()) 
            elist = EntitiesList(objects, **params)
            self.thread_actor.list(params, elist.objects)
        log.write('And list posts in them')
        for params in constants.TEST_THREADS['listPosts']:
            thread = random.choice(self.threads.values())
            params['thread'] = thread.id
            objects = copy.deepcopy([p for p in self.posts.values() if p.thread == thread.id]) 
            elist = EntitiesList(objects, **params)
            self.thread_actor.list_posts(params, elist.objects)        
        thread = random.choice(self.threads.values())
        thread_posts = EntitiesList([p for p in self.posts.values() if p.thread == thread.id], order='desc')
        log.write('Go away thread!')
        self.thread_actor.remove({'thread': thread.id}, thread, thread_posts.objects)
        log.write('Alright, I forgive you, come back')
        self.thread_actor.restore({'thread': thread.id}, thread, thread_posts.objects)
        log.write('Changed my mind again, goodbye!')
        self.thread_actor.close({'thread': thread.id}, thread)
        log.write('But I cant live without you')
        self.thread_actor.open({'thread': thread.id}, thread)
        log.write('Update post')
        self.thread_actor.update({'thread': thread.id, 'message': thread.message, 'slug': 'newslug'}, thread)
        log.write('Likes time...again!')
        for _ in range(constants.TEST_THREADS['votes']):
            thread = random.choice(self.threads.values())
            vote = random.choice([1, -1])
            self.thread_actor.vote({'thread': thread.id, 'vote': vote}, thread)
        log.write('Subscribe me')
        for _ in range(constants.TEST_THREADS['subscriptions']):
            thread = random.choice(self.threads.values())
            user = random.choice(self.users.values())
            self.thread_actor.subscribe({'thread': thread.id, 'user': user.unique_id}, thread)
        log.write('Unsubscribe me')
        for _ in range(constants.TEST_THREADS['unsubscriptions']):
            thread = random.choice(self.threads.values())
            user = random.choice(self.users.values())
            self.thread_actor.unsubscribe({'thread': thread.id, 'user': user.unique_id}, thread)

    def test_users(self):
        # print 'TEST USERS'
        log.write('OMG, I was soooooo wasted...what did I wrote yesterday?')
        for params in constants.TEST_USERS['listPosts']:
            objects = copy.deepcopy([p for p in self.posts.values() if p.user == params['user']]) 
            elist = EntitiesList(objects, **params)
            self.user_actor.list_posts(params, elist.objects)
        log.write('It was huge mistake. Need to change a nick quickly')
        for params in constants.TEST_USERS['updateProfile']:
            user = self.users[params['user']]
            self.user_actor.update_profile(params, user)
        log.write('Follow someone')
        for params in constants.TEST_USERS['follow']:
            follower = self.users[params['follower']]
            followee = self.users[params['followee']]
            self.user_actor.follow(params, follower, followee)
        log.write('List followers')
        for params in constants.TEST_USERS['listFollowers']:
            user = self.users[params['user']]            
            del params['user']     
            objects = copy.deepcopy([self.users[u] for u in user.followers]) 
            elist = EntitiesList(objects, **params)
            params['user'] = user.email
            self.user_actor.list_followers(params, elist.objects)
        log.write('List following')
        for params in constants.TEST_USERS['listFollowing']:
            user = self.users[params['user']]       
            del params['user']     
            objects = copy.deepcopy([self.users[u] for u in user.following]) 
            elist = EntitiesList(objects, **params)
            params['user'] = user.email
            self.user_actor.list_following(params, elist.objects)
        log.write('Unfollow someone')
        for params in constants.TEST_USERS['unfollow']:
            follower = self.users[params['follower']]
            followee = self.users[params['followee']]
            self.user_actor.unfollow(params, follower, followee)

def produce_docs(with_toc=False):
    tpl = open('../doc/doc_template.md').read()
    toc = {}
    for doc_path, context in docs.iteritems():
        doc_fn = os.path.basename(doc_path)
        doc_dir = os.path.dirname(doc_path)
        if not os.path.exists(doc_dir):
            os.makedirs(doc_dir)

        context['description'] = DISCR[context['entity_name']]['methods'][context['entity_method']]
        context['header'] = context['entity_name'].capitalize() + '.' + context['entity_method']
        for arg_type in ('optional', 'requried'):
            fields = copy.deepcopy(context[arg_type])
            context[arg_type] = ''
            for field in fields:
                context[arg_type] += '* ' + field + '\n\n'
                context[arg_type] += '   ' + DISCR[context['entity_name']]['fields'][field] + '\n'

            if context[arg_type]:
                context[arg_type] =  '###%s\n' % arg_type.capitalize() + context[arg_type]
        with open(doc_path, 'w') as fd:
            fd.write(tpl % context)

        entity, method = context['header'].split('.')
        if entity not in toc:
            toc[entity] = []
        toc[entity].append((method, os.path.join('./doc/', entity.lower(), doc_fn)))
    if with_toc:
        with open('../README.md', 'a') as readme:
            for entity in toc:
                readme.write('##' + entity + '\n')
                for method, url in sorted(toc[entity], key=lambda t: t[0]):
                    readme.write('* [%s](%s)\n' % (method, url))
                readme.write('\n')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-v", "--verbose", dest="verbose",
                      action="store_true", default=False, help="log to stdout")
    parser.add_option("-a", "--address", dest="ip_port",
                      action="store", type="string", default='127.0.0.1:5000')
    (options, args) = parser.parse_args()
    TESTS = {}
    log = TestLog(options.verbose)
    log.write('Testing started for: %s' % options.ip_port)
    passed = True
    try:
        testsuite = TestScenario(student_ip=options.ip_port)
        testsuite.start()
    except ValueError:
        passed = False

    num_passed_tests = sum(1 for t in TESTS.values() if t)
    passed = True if num_passed_tests == len(TESTS) else False

    if not passed and not options.verbose:
        for line in log.test_log:
            print '%s: %s\n' % (line['level'], line['message'])
    pprint.pprint(TESTS)
    passed_str = '%d/%d' % (num_passed_tests, len(TESTS))
    print passed_str + ' tests passed'
