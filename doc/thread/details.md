#Thread.details
Get thread details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* related

   ```array``` include related entities. Possible values: ```['user', 'forum']```. Default: []


###Requried
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/details/ with ```{'thread': 681}```:
```json
{u'code': 0,
 u'response': {u'date': u'2013-12-30 00:01:01',
               u'dislikes': 0,
               u'forum': u'forum3',
               u'id': 681,
               u'isClosed': False,
               u'isDeleted': True,
               u'likes': 0,
               u'message': u'hey hey!',
               u'points': 0,
               u'posts': 1,
               u'slug': u'thread2',
               u'title': u'Thread II',
               u'user': u'richard.nixon@example.com'}}
```
