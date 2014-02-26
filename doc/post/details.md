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

Requesting http://some.host.ru/db/api/s.stupnikov/post/details/ with _{'post': 184, 'related': ['thread', 'forum', 'user']}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'dislikes': 0,
               u'forum': {u'id': 950,
                          u'name': u'\u0424\u043e\u0440\u0443\u043c \u0422\u0440\u0438',
                          u'short_name': u'forum3',
                          u'user': u'example3@mail.ru'},
               u'id': 184,
               u'isApproved': True,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': True,
               u'isSpam': False,
               u'likes': 0,
               u'message': u'my message 1',
               u'parent': None,
               u'points': 0,
               u'thread': {u'date': u'2013-12-31 00:01:01',
                           u'dislikes': 0,
                           u'forum': u'forum3',
                           u'id': 803,
                           u'isClosed': False,
                           u'isDeleted': False,
                           u'likes': 0,
                           u'message': u'hey!',
                           u'points': 0,
                           u'posts': 1,
                           u'slug': u'thread1',
                           u'title': u'Thread I',
                           u'user': u'example@mail.ru'},
               u'user': {u'about': u'hello im user3',
                         u'email': u'example3@mail.ru',
                         u'followers': [],
                         u'following': [],
                         u'id': 79,
                         u'isAnonymous': False,
                         u'name': u'Josh',
                         u'subscriptions': [],
                         u'username': u'user3'}}}
```
