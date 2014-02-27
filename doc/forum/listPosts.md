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
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listPosts/ with _{'related': ['thread'], 'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'forum': 'forumwithsufficientlylargename'}_:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-02 00:02:01',
                u'dislikes': 0,
                u'forum': u'forumwithsufficientlylargename',
                u'id': 798,
                u'isApproved': False,
                u'isDeleted': False,
                u'isEdited': True,
                u'isHighlighted': False,
                u'isSpam': True,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': 334,
                u'points': 0,
                u'thread': {u'date': u'2014-01-01 00:00:01',
                            u'dislikes': 0,
                            u'forum': u'forumwithsufficientlylargename',
                            u'id': 541,
                            u'isClosed': True,
                            u'isDeleted': True,
                            u'likes': 0,
                            u'message': u'hey hey hey hey!',
                            u'points': 0,
                            u'posts': 3,
                            u'slug': u'Threadwithsufficientlylargetitle',
                            u'title': u'Thread With Sufficiently Large Title',
                            u'user': u'example4@mail.ru'},
                u'user': u'example3@mail.ru'}]}
```
