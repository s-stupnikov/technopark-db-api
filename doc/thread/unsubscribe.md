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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/unsubscribe/ with **{'user': 'example@mail.ru', 'thread': 504}**:
```json
{u'code': 0, u'response': {u'thread': 504, u'user': u'example@mail.ru'}}
```
