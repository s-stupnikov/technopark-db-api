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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/update/ with **{'message': 'hey hey hey hey!', 'slug': 'newslug', 'thread': 504}**:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'dislikes': 0,
               u'forum': u'forumwithsufficientlylargename',
               u'id': 504,
               u'isClosed': False,
               u'isDeleted': False,
               u'likes': 0,
               u'message': u'hey hey hey hey!',
               u'points': 0,
               u'posts': 0,
               u'slug': u'newslug',
               u'title': u'Thread With Sufficiently Large Title',
               u'user': u'example2@mail.ru'}}
```
