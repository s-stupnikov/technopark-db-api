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


Requesting http://some.host.ru/db/api/s.stupnikov/post/vote/ with _{'vote': -1, 'post': 463}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-03 00:08:01',
               u'dislikes': 1,
               u'forum': u'forumwithsufficientlylargename',
               u'id': 463,
               u'isApproved': False,
               u'isDeleted': True,
               u'isEdited': False,
               u'isHighlighted': False,
               u'isSpam': False,
               u'likes': 0,
               u'message': u'my message 1',
               u'parent': None,
               u'points': -1,
               u'thread': 36,
               u'user': u'richard.nixon@example.com'}}
```
