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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/vote/ with **{'vote': -1, 'thread': 560}**:
```json
{u'code': 0,
 u'response': {u'date': u'2013-12-31 00:01:01',
               u'dislikes': 1,
               u'forum': u'forumwithsufficientlylargename',
               u'id': 560,
               u'isClosed': False,
               u'isDeleted': False,
               u'likes': 0,
               u'message': u'hey!',
               u'points': -1,
               u'posts': 1,
               u'slug': u'thread1',
               u'title': u'Thread I',
               u'user': u'example2@mail.ru'}}
```
