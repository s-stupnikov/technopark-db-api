#Thread.update
Edit thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* message
   ```str``` thread message
* slug
   ```str``` thread slug
* thread
   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/update/ with _{'message': 'hey hey!', 'slug': 'newslug', 'thread': 397}_:
```json
{u'code': 0,
 u'response': {u'date': u'2013-12-30 00:01:01',
               u'dislikes': 0,
               u'forum': u'forum2',
               u'id': 397,
               u'isClosed': False,
               u'isDeleted': False,
               u'likes': 0,
               u'message': u'hey hey!',
               u'points': 0,
               u'posts': 1,
               u'slug': u'newslug',
               u'title': u'Thread II',
               u'user': u'example3@mail.ru'}}
```
