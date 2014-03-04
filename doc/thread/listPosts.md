#Thread.listPosts
Get posts from this thread

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* since

   ```str``` include threads created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/listPosts/ with **{'since': '2014-01-01 00:00:00', 'order': 'desc', 'thread': 709}**:
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
                u'user': u'example@mail.ru'},
               {u'date': u'2014-01-01 00:02:01',
                u'dislikes': 0,
                u'forum': u'forum1',
                u'id': 780,
                u'isApproved': False,
                u'isDeleted': False,
                u'isEdited': True,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 3',
                u'parent': 723,
                u'points': 0,
                u'thread': 709,
                u'user': u'example3@mail.ru'},
               {u'date': u'2014-01-01 00:00:01',
                u'dislikes': 1,
                u'forum': u'forum1',
                u'id': 723,
                u'isApproved': True,
                u'isDeleted': False,
                u'isEdited': True,
                u'isHighlighted': True,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': -1,
                u'thread': 709,
                u'user': u'example@mail.ru'}]}
```
