#Post.update
Edit post

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* post

   ```int``` post id
* message

   ```str``` post body


Requesting http://some.host.ru/db/api/s.stupnikov/post/update/ with **{'post': 18, 'message': 'my message 1'}**:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-03 00:01:01',
               u'dislikes': 0,
               u'forum': u'forum2',
               u'id': 18,
               u'isApproved': True,
               u'isDeleted': False,
               u'isEdited': False,
               u'isHighlighted': False,
               u'isSpam': False,
               u'likes': 0,
               u'message': u'my message 1',
               u'parent': None,
               u'points': 0,
               u'thread': 348,
               u'user': u'example4@mail.ru'}}
```
