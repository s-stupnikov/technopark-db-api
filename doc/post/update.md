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


Requesting http://some.host.ru/db/api/s.stupnikov/post/update/ with ```{'post': 990, 'message': 'my message 3'}```:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:02:01',
               u'dislikes': 0,
               u'forum': u'forum3',
               u'id': 990,
               u'isApproved': False,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': False,
               u'isSpam': False,
               u'likes': 0,
               u'message': u'my message 3',
               u'parent': 243,
               u'points': 0,
               u'thread': 311,
               u'user': u'example2@mail.ru'}}
```
