#Thread.update
Edit thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* message

   ```str``` thread message
* slug

   ```str``` thread slug
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/update/ with _{'message': 'hey hey hey!', 'slug': 'newslug', 'thread': 848}_:
```json
{u'code': 0,
 u'response': {u'date': u'2013-12-29 00:01:01',
               u'dislikes': 0,
               u'forum': u'forum1',
               u'id': 848,
               u'isClosed': False,
               u'isDeleted': False,
               u'likes': 0,
               u'message': u'hey hey hey!',
               u'points': 0,
               u'posts': 3,
               u'slug': u'newslug',
               u'title': u'\u0422\u0440\u0435\u0434 \u0422\u0440\u0438',
               u'user': u'example3@mail.ru'}}
```
