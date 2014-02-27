#User.listPosts
Get posts from this user

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* since

   ```str``` include posts from this user created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit
* order

   ```str``` sort order (by name). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user

   ```str``` user email


Requesting http://some.host.ru/db/api/s.stupnikov/user/listPosts/ with _{'since': '2014-01-03 00:00:00', 'limit': 3, 'user': 'example3@mail.ru', 'order': 'desc'}_:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-03 00:08:01',
                u'dislikes': 0,
                u'forum': u'forum3',
                u'id': 162,
                u'isApproved': False,
                u'isDeleted': False,
                u'isEdited': False,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': 0,
                u'thread': 184,
                u'user': u'example3@mail.ru'},
               {u'date': u'2014-01-03 00:01:01',
                u'dislikes': 0,
                u'forum': u'forum3',
                u'id': 585,
                u'isApproved': True,
                u'isDeleted': False,
                u'isEdited': False,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': 0,
                u'thread': 184,
                u'user': u'example3@mail.ru'}]}
```
