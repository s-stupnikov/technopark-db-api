import func_test
from func_test_constants import TEST_CONF, TEST_THREADS

def print_el(el):
    for item in el.objects:
        print "- {}: {}".format(item.id, item.date)

def generate_beautyfull_tree(posts):
    new_posts = {}
    for post in posts:
        new_post = {'children': {}, 'id': post.id}
        if (post.parent is not None):
            new_post['parent'] = post.parent
            new_posts[post.parent]['children'][post.id] = new_post
        new_posts[post.id] = new_post
    def _print_posts_recursive(posts, level=1):
        for post_id in sorted(posts.iterkeys()):
            post = posts[post_id]
            if level == 1 and (post.get('parent') is not None):
                continue
            print '-' * level, ' ', post_id
            _print_posts_recursive(post['children'], level + 1)
    _print_posts_recursive(new_posts)
            
        
threads = {}
posts = []

for index, thread in enumerate(TEST_CONF['threads']):
    thread['id'] = index
    threads[index] = thread


tsc = func_test.TestScenario(threads, TEST_CONF)

tsc._create_posts(posts)

for post in posts:
    print post

print '********** beautifull tree ***********'
generate_beautyfull_tree(posts)

for conf in TEST_THREADS['listPosts']:
    #print conf
    print '\n\n***** sorted *****'
    el = func_test.EntitiesList(posts, **conf)
    print conf
    print_el(el)
