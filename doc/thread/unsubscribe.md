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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/unsubscribe/ with ```{'user': 'richard.nixon@example.com', 'thread': 681}```:
```json
{u'code': 0,
 u'response': {u'thread': 681, u'user': u'richard.nixon@example.com'}}
```
