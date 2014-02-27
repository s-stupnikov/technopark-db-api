#Post.details
Get post details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments


###Requried
* post
   ```int``` post id


Requesting http://some.host.ru/db/api/s.stupnikov/post/details/ with _{'post': 432}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-02 00:02:01',
               u'dislikes': 0,
               u'forum': u'forum3',
               u'id': 432,
               u'isApproved': False,
               u'isDeleted': True,
               u'isEdited': True,
               u'isHighlighted': False,
               u'isSpam': True,
               u'likes': 0,
               u'message': u'my message 1',
               u'parent': 748,
               u'points': 0,
               u'thread': 768,
               u'user': u'example@mail.ru'}}
```
