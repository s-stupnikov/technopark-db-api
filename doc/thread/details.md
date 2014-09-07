#Thread.details
Get thread details

## Supported request methods 
* GET

##Arguments
###Optional
* related

   ```array``` include related entities. Possible values: ```['user', 'forum']```. Default: []


###Requried
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/details/ with **{'thread': 504}**:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'dislikes': 0,
               u'forum': u'forumwithsufficientlylargename',
               u'id': 504,
               u'isClosed': True,
               u'isDeleted': True,
               u'likes': 0,
               u'message': u'hey hey hey hey!',
               u'points': 0,
               u'posts': 0,
               u'slug': u'Threadwithsufficientlylargetitle',
               u'title': u'Thread With Sufficiently Large Title',
               u'user': u'example2@mail.ru'}}
```
