#Thread.vote
like/dislike thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* vote

   ```int``` like/dislike. Possible values: [1, -1]
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/vote/ with _{'vote': 1, 'thread': 295}_:
```json
{u'code': 0,
 u'response': {u'date': u'2013-12-30 00:01:01',
               u'dislikes': 0,
               u'forum': u'forumwithsufficientlylargename',
               u'id': 295,
               u'isClosed': False,
               u'isDeleted': False,
               u'likes': 1,
               u'message': u'hey hey!',
               u'points': 1,
               u'posts': 0,
               u'slug': u'thread2',
               u'title': u'Thread II',
               u'user': u'example2@mail.ru'}}
```
