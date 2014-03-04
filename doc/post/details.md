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


Requesting http://some.host.ru/db/api/s.stupnikov/post/details/ with **{'post': 723}**:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'dislikes': 0,
               u'forum': u'forum1',
               u'id': 723,
               u'isApproved': True,
               u'isDeleted': True,
               u'isEdited': True,
               u'isHighlighted': True,
               u'isSpam': False,
               u'likes': 0,
               u'message': u'my message 1',
               u'parent': None,
               u'points': 0,
               u'thread': 709,
               u'user': u'example@mail.ru'}}
```
