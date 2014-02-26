#Thread.details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* related
###Requried
* thread

Requesting http://some.host.ru/db/api/s.stupnikov/thread/details/ with _{'related': ['forum', 'user'], 'thread': 548}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'dislikes': 0,
               u'forum': {u'id': 74,
                          u'name': u'Forum I',
                          u'short_name': u'forum1',
                          u'user': u'richard.nixon@example.com'},
               u'id': 548,
               u'isClosed': True,
               u'isDeleted': True,
               u'likes': 0,
               u'message': u'hey hey hey hey!',
               u'points': 0,
               u'posts': 0,
               u'slug': u'Threadwithsufficientlylargetitle',
               u'title': u'Thread With Sufficiently Large Title',
               u'user': {u'about': u'hello im user3',
                         u'email': u'example3@mail.ru',
                         u'followers': [],
                         u'following': [],
                         u'id': 621,
                         u'isAnonymous': False,
                         u'name': u'Josh',
                         u'subscriptions': [],
                         u'username': u'user3'}}}
```
