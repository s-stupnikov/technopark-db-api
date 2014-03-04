#Post.details
Get post details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* related

   ```array``` include related entities. Possible values: ```['user', 'thread', 'forum']```. Default: []


###Requried
* post

   ```int``` post id


Requesting http://some.host.ru/db/api/s.stupnikov/post/details/ with _{'post': 634}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:02:01',
               u'dislikes': 0,
               u'forum': u'forumwithsufficientlylargename',
               u'id': 634,
               u'isApproved': False,
               u'isDeleted': True,
               u'isEdited': True,
               u'isHighlighted': False,
               u'isSpam': False,
               u'likes': 0,
               u'message': u'my message 3',
               u'parent': 872,
               u'points': 0,
               u'thread': 668,
               u'user': u'example4@mail.ru'}}
```
