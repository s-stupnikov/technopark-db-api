#Forum.listPosts

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order
* since
###Requried
* forum

Requesting http://some.host.ru/db/api/s.stupnikov/forum/listPosts/ with _{'related': ['thread'], 'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'forum': 'forumwithsufficientlylargename'}_:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-03 00:01:01',
                u'dislikes': 0,
                u'forum': u'forumwithsufficientlylargename',
                u'id': 29,
                u'isApproved': True,
                u'isDeleted': False,
                u'isEdited': False,
                u'isHighlighted': False,
                u'isSpam': False,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': None,
                u'points': 0,
                u'thread': {u'date': u'2013-12-31 00:01:01',
                            u'dislikes': 0,
                            u'forum': u'forumwithsufficientlylargename',
                            u'id': 182,
                            u'isClosed': False,
                            u'isDeleted': False,
                            u'likes': 0,
                            u'message': u'hey!',
                            u'points': 0,
                            u'posts': 1,
                            u'slug': u'thread1',
                            u'title': u'Thread I',
                            u'user': u'example@mail.ru'},
                u'user': u'example4@mail.ru'}]}
```
