#Post.create

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional
* isSpam
* isEdited
* isDeleted
* isHighlighted
* isApproved
###Requried
* user
* thread
* date
* message
* forum

Requesting http://some.host.ru/db/api/s.stupnikov/post/create/ with _{'isApproved': True, 'user': 'example2@mail.ru', 'date': '2014-01-01 00:00:01', 'message': 'my message 1', 'isSpam': False, 'isHighlighted': True, 'thread': 548, 'forum': 'forum1', 'isDeleted': False, 'isEdited': True}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'forum': u'forum1',
               u'id': 832,
               u'isApproved': True,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': True,
               u'isSpam': False,
               u'message': u'my message 1',
               u'thread': 548,
               u'user': u'example2@mail.ru'}}
```
