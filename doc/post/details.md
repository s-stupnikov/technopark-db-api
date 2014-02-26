#Post.details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* related
###Requried
* post

Requesting http://some.host.ru/db/api/s.stupnikov/post/details/ with _{'post': 832, 'related': ['thread', 'forum', 'user']}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'dislikes': 0,
               u'forum': {u'id': 74,
                          u'name': u'Forum I',
                          u'short_name': u'forum1',
                          u'user': u'richard.nixon@example.com'},
               u'id': 832,
               u'isApproved': True,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': True,
               u'isSpam': False,
               u'likes': 0,
               u'message': u'my message 1',
               u'parent': None,
               u'points': 0,
               u'thread': {u'date': u'2014-01-01 00:00:01',
                           u'dislikes': 0,
                           u'forum': u'forum1',
                           u'id': 548,
                           u'isClosed': True,
                           u'isDeleted': True,
                           u'likes': 0,
                           u'message': u'hey hey hey hey!',
                           u'points': 0,
                           u'posts': 1,
                           u'slug': u'Threadwithsufficientlylargetitle',
                           u'title': u'Thread With Sufficiently Large Title',
                           u'user': u'example3@mail.ru'},
               u'user': {u'about': u'hello im user2',
                         u'email': u'example2@mail.ru',
                         u'followers': [],
                         u'following': [],
                         u'id': 14,
                         u'isAnonymous': False,
                         u'name': u'Jey',
                         u'subscriptions': [],
                         u'username': u'user2'}}}
```
