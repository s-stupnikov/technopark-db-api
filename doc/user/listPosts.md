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

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user

   ```str``` user email


Requesting http://some.host.ru/db/api/s.stupnikov/user/listPosts/ with **{'since': '2014-01-01 00:00:00', 'user': 'example2@mail.ru', 'order': 'asc'}**:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-01 00:00:01',
                u'dislikes': 1,
                u'forum': u'forumwithsufficientlylargename',
                u'id': 881,
                u'isApproved': True,
                u'isDeleted': False,
                u'isEdited': True,
                u'isHighlighted': True,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': -1,
                u'thread': 297,
                u'user': u'example2@mail.ru'}]}
```
