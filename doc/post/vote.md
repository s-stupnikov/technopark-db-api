#Post.vote

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional


###Requried
* post
* vote

Requesting http://some.host.ru/db/api/s.stupnikov/post/vote/ with _{'vote': -1, 'post': 285}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-03 00:08:01',
               u'dislikes': 1,
               u'forum': u'forum3',
               u'id': 285,
               u'isApproved': False,
               u'isDeleted': True,
               u'isEdited': False,
               u'isHighlighted': False,
               u'isSpam': False,
               u'likes': 0,
               u'message': u'my message 1',
               u'parent': None,
               u'points': -1,
               u'thread': 803,
               u'user': u'example4@mail.ru'}}
```
