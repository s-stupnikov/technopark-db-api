#Thread.details
Get thread details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* related

   ```array``` include related entities. Possible values: ```['user', 'forum']```. Default: []


###Requried
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/details/ with _{'thread': 256}_:
```json
{u'code': 0,
 u'response': {u'date': u'2013-12-29 00:01:01',
               u'dislikes': 0,
               u'forum': u'forum3',
               u'id': 256,
               u'isClosed': False,
               u'isDeleted': True,
               u'likes': 0,
               u'message': u'hey hey hey!',
               u'points': 0,
               u'posts': 0,
               u'slug': u'thread3',
               u'title': u'\u0422\u0440\u0435\u0434 \u0422\u0440\u0438',
               u'user': u'example4@mail.ru'}}
```
