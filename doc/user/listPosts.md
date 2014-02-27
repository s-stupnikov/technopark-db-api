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
* order
   ```str``` sort order (by name). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user
   ```str``` user email


Requesting http://some.host.ru/db/api/s.stupnikov/user/listPosts/ with _{'since': '2014-01-02 00:00:00', 'limit': 2, 'user': 'example@mail.ru', 'order': 'asc'}_:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-02 00:02:01',
                u'dislikes': 0,
                u'forum': u'forum3',
                u'id': 432,
                u'isApproved': False,
                u'isDeleted': False,
                u'isEdited': True,
                u'isHighlighted': False,
                u'isSpam': True,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': 748,
                u'points': 0,
                u'thread': 768,
                u'user': u'example@mail.ru'},
               {u'date': u'2014-01-03 00:01:01',
                u'dislikes': 0,
                u'forum': u'forum2',
                u'id': 900,
                u'isApproved': True,
                u'isDeleted': False,
                u'isEdited': False,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': 0,
                u'thread': 47,
                u'user': u'example@mail.ru'}]}
```
