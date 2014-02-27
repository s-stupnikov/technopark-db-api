#Thread.unsubscribe
Unsubscribe user from this thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* user
   ```str``` founder email
* thread
   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/unsubscribe/ with _{'user': 'example3@mail.ru', 'thread': 282}_:
```json
{u'code': 0, u'response': {u'thread': 282, u'user': u'example3@mail.ru'}}
```
