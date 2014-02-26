#Thread.vote

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional

###Requried
* thread
* vote

Requesting http://some.host.ru/db/api/s.stupnikov/thread/vote/ with _{'vote': -1, 'thread': 182}_:
```json
{u'code': 0,
 u'response': {u'date': u'2013-12-31 00:01:01',
               u'dislikes': 1,
               u'forum': u'forumwithsufficientlylargename',
               u'id': 182,
               u'isClosed': False,
               u'isDeleted': False,
               u'likes': 0,
               u'message': u'hey!',
               u'points': -1,
               u'posts': 1,
               u'slug': u'thread1',
               u'title': u'Thread I',
               u'user': u'example@mail.ru'}}
```
