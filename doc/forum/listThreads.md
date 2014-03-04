#Forum.listThreads
Get threads from this forum

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* since

   ```str``` include forums created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'
* related

   ```array``` include related entities. Possible values: ```['user',]```. Default: []


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listThreads/ with _{'since': '2013-12-29 00:00:00', 'limit': 3, 'order': 'desc', 'forum': 'forum3'}_:
```json
{u'code': 0,
 u'response': [{u'date': u'2013-12-29 00:01:01',
                u'dislikes': 0,
                u'forum': u'forum3',
                u'id': 256,
                u'isClosed': False,
                u'isDeleted': False,
                u'likes': 0,
                u'message': u'hey hey hey!',
                u'points': 0,
                u'posts': 0,
                u'slug': u'thread3',
                u'title': u'\u0422\u0440\u0435\u0434 \u0422\u0440\u0438',
                u'user': u'example4@mail.ru'}]}
```
