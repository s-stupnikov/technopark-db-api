#Thread.create

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional
* isDeleted
###Requried
* message
* user
* date
* slug
* title
* isClosed
* forum

Requesting http://some.host.ru/db/api/s.stupnikov/thread/create/ with _{'forum': 'forum1', 'title': 'Thread With Sufficiently Large Title', 'isClosed': True, 'user': 'example3@mail.ru', 'date': '2014-01-01 00:00:01', 'message': 'hey hey hey hey!', 'slug': 'Threadwithsufficientlylargetitle', 'isDeleted': True}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'forum': u'forum1',
               u'id': 548,
               u'isClosed': True,
               u'isDeleted': True,
               u'message': u'hey hey hey hey!',
               u'slug': u'Threadwithsufficientlylargetitle',
               u'title': u'Thread With Sufficiently Large Title',
               u'user': u'example3@mail.ru'}}
```
