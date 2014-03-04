#Post.list
List posts

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* since

   ```str``` include posts created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* forum

   ```str``` forum short_name
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/post/list/ with _{'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'forum': 'forumwithsufficientlylargename'}_:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-03 00:08:01',
                u'dislikes': 0,
                u'forum': u'forumwithsufficientlylargename',
                u'id': 463,
                u'isApproved': False,
                u'isDeleted': True,
                u'isEdited': False,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': 0,
                u'thread': 36,
                u'user': u'richard.nixon@example.com'}]}
```
