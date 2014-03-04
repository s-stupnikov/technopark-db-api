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


Requesting http://some.host.ru/db/api/s.stupnikov/user/listPosts/ with ```{'since': '2014-01-01 00:00:00', 'user': 'example2@mail.ru', 'order': 'asc'}```:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-01 00:02:01',
                u'dislikes': 0,
                u'forum': u'forum3',
                u'id': 990,
                u'isApproved': False,
                u'isDeleted': False,
                u'isEdited': True,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 3',
                u'parent': 243,
                u'points': 0,
                u'thread': 311,
                u'user': u'example2@mail.ru'}]}
```
