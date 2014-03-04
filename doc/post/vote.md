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


Requesting http://some.host.ru/db/api/s.stupnikov/post/vote/ with _{'vote': 1, 'post': 634}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:02:01',
               u'dislikes': 0,
               u'forum': u'forumwithsufficientlylargename',
               u'id': 634,
               u'isApproved': False,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': False,
               u'isSpam': False,
               u'likes': 1,
               u'message': u'my message 3',
               u'parent': 872,
               u'points': 1,
               u'thread': 668,
               u'user': u'example4@mail.ru'}}
```
