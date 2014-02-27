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
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listThreads/ with _{'related': ['forum'], 'since': '2013-12-31 00:00:00', 'order': 'desc', 'forum': 'forum1'}_:
```json
{u'code': 0,
 u'response': [{u'date': u'2013-12-31 00:01:01',
                u'dislikes': 0,
                u'forum': {u'id': 204,
                           u'name': u'Forum I',
                           u'short_name': u'forum1',
                           u'user': u'example3@mail.ru'},
                u'id': 358,
                u'isClosed': False,
                u'isDeleted': False,
                u'likes': 0,
                u'message': u'hey!',
                u'points': 0,
                u'posts': 0,
                u'slug': u'thread1',
                u'title': u'Thread I',
                u'user': u'example2@mail.ru'}]}
```
