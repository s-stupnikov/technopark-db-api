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

Requesting http://some.host.ru/db/api/s.stupnikov/post/vote/ with _{'vote': 1, 'post': 832}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'dislikes': 0,
               u'forum': u'forum1',
               u'id': 832,
               u'isApproved': True,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': True,
               u'isSpam': False,
               u'likes': 1,
               u'message': u'my message 1',
               u'parent': None,
               u'points': 1,
               u'thread': 548,
               u'user': u'example2@mail.ru'}}
```
