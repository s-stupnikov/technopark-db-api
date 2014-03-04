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


Requesting http://some.host.ru/db/api/s.stupnikov/post/details/ with **{'post': 18}**:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-03 00:01:01',
               u'dislikes': 0,
               u'forum': u'forum2',
               u'id': 18,
               u'isApproved': True,
               u'isDeleted': True,
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
