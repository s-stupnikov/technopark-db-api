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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/subscribe/ with ```{'user': 'richard.nixon@example.com', 'thread': 311}```:
```json
{u'code': 0,
 u'response': {u'thread': 311, u'user': u'richard.nixon@example.com'}}
```
