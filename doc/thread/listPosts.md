#Thread.listPosts
Get posts from this thread

## Supported request methods 
* GET

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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/listPosts/ with **{'since': '2014-01-01 00:00:00', 'order': 'desc', 'thread': 348}**:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-03 00:08:01',
                u'dislikes': 0,
                u'forum': u'forum2',
                u'id': 487,
                u'isApproved': False,
                u'isDeleted': True,
                u'isEdited': False,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': 0,
                u'thread': 348,
                u'user': u'richard.nixon@example.com'},
               {u'date': u'2014-01-03 00:01:01',
                u'dislikes': 0,
                u'forum': u'forum2',
                u'id': 18,
                u'isApproved': True,
                u'isDeleted': False,
                u'isEdited': False,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': 0,
                u'thread': 348,
                u'user': u'example4@mail.ru'}]}
```
