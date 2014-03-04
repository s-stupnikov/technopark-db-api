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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/vote/ with ```{'vote': -1, 'thread': 311}```:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'dislikes': 1,
               u'forum': u'forum3',
               u'id': 311,
               u'isClosed': True,
               u'isDeleted': True,
               u'likes': 0,
               u'message': u'hey hey hey hey!',
               u'points': -1,
               u'posts': 3,
               u'slug': u'Threadwithsufficientlylargetitle',
               u'title': u'Thread With Sufficiently Large Title',
               u'user': u'example3@mail.ru'}}
```
