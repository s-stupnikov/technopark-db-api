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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/unsubscribe/ with **{'user': 'example4@mail.ru', 'thread': 709}**:
```json
{u'code': 0, u'response': {u'thread': 709, u'user': u'example4@mail.ru'}}
```
