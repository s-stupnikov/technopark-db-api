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


Requesting http://some.host.ru/db/api/s.stupnikov/post/vote/ with **{'vote': -1, 'post': 881}**:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'dislikes': 1,
               u'forum': u'forumwithsufficientlylargename',
               u'id': 881,
               u'isApproved': True,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': True,
               u'isSpam': False,
               u'likes': 0,
               u'message': u'my message 1',
               u'parent': None,
               u'points': -1,
               u'thread': 297,
               u'user': u'example2@mail.ru'}}
```
