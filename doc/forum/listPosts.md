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

   ```array``` include related entities. Possible values: ```['user',]```. Default: []


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listPosts/ with _{'related': ['thread'], 'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'forum': 'forumwithsufficientlylargename'}_:
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
                u'thread': {u'date': u'2013-12-30 00:01:01',
                            u'dislikes': 0,
                            u'forum': u'forumwithsufficientlylargename',
                            u'id': 36,
                            u'isClosed': False,
                            u'isDeleted': False,
                            u'likes': 0,
                            u'message': u'hey hey!',
                            u'points': 0,
                            u'posts': 1,
                            u'slug': u'thread2',
                            u'title': u'Thread II',
                            u'user': u'example2@mail.ru'},
                u'user': u'richard.nixon@example.com'}]}
```
