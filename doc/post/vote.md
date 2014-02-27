#Post.vote
like/dislike post

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* vote
   ```int``` like/dislike. Possible values: [1, -1]
* post
   ```int``` post id


Requesting http://some.host.ru/db/api/s.stupnikov/post/vote/ with _{'vote': 1, 'post': 236}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-03 00:08:01',
               u'dislikes': 0,
               u'forum': u'forum2',
               u'id': 236,
               u'isApproved': False,
               u'isDeleted': True,
               u'isEdited': False,
               u'isHighlighted': False,
               u'isSpam': False,
               u'likes': 1,
               u'message': u'my message 1',
               u'parent': None,
               u'points': 1,
               u'thread': 397,
               u'user': u'richard.nixon@example.com'}}
```
