#Thread.subscribe
Subscribe user to this thread

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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/subscribe/ with _{'user': 'example2@mail.ru', 'thread': 295}_:
```json
{u'code': 0, u'response': {u'thread': 295, u'user': u'example2@mail.ru'}}
```
