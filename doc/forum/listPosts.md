#Forum.listPosts
Get posts from this forum

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* since

   ```str``` include forums created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'
* related

   ```array``` include related entities. Possible values: ```['thread', 'forum', 'user']```. Default: []


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listPosts/ with **{'related': ['thread'], 'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'forum': 'forumwithsufficientlylargename'}**:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-02 00:02:01',
                u'dislikes': 0,
                u'forum': u'forumwithsufficientlylargename',
                u'id': 315,
                u'isApproved': False,
                u'isDeleted': False,
                u'isEdited': True,
                u'isHighlighted': False,
                u'isSpam': True,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': 32,
                u'points': 0,
                u'thread': {u'date': u'2013-12-31 00:01:01',
                            u'dislikes': 0,
                            u'forum': u'forumwithsufficientlylargename',
                            u'id': 297,
                            u'isClosed': False,
                            u'isDeleted': False,
                            u'likes': 0,
                            u'message': u'hey!',
                            u'points': 0,
                            u'posts': 3,
                            u'slug': u'thread1',
                            u'title': u'Thread I',
                            u'user': u'example4@mail.ru'},
                u'user': u'richard.nixon@example.com'}]}
```
