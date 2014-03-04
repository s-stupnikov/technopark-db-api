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


Requesting http://some.host.ru/db/api/s.stupnikov/user/listPosts/ with **{'since': '2014-01-02 00:00:00', 'limit': 2, 'user': 'example@mail.ru', 'order': 'asc'}**:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-02 00:02:01',
                u'dislikes': 0,
                u'forum': u'forum1',
                u'id': 807,
                u'isApproved': False,
                u'isDeleted': False,
                u'isEdited': True,
                u'isHighlighted': False,
                u'isSpam': True,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': 780,
                u'points': 0,
                u'thread': 709,
                u'user': u'example@mail.ru'}]}
```
