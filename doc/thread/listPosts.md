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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/listPosts/ with _{'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'thread': 965}_:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-03 00:01:01',
                u'dislikes': 0,
                u'forum': u'forum3',
                u'id': 156,
                u'isApproved': True,
                u'isDeleted': False,
                u'isEdited': False,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': 0,
                u'thread': 965,
                u'user': u'richard.nixon@example.com'}]}
```
