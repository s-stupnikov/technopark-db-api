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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/vote/ with _{'vote': 1, 'thread': 256}_:
```json
{u'code': 0,
 u'response': {u'date': u'2013-12-29 00:01:01',
               u'dislikes': 0,
               u'forum': u'forum3',
               u'id': 256,
               u'isClosed': False,
               u'isDeleted': False,
               u'likes': 1,
               u'message': u'hey hey hey!',
               u'points': 1,
               u'posts': 0,
               u'slug': u'newslug',
               u'title': u'\u0422\u0440\u0435\u0434 \u0422\u0440\u0438',
               u'user': u'example4@mail.ru'}}
```
