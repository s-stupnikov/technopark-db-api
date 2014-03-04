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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/subscribe/ with **{'user': 'example3@mail.ru', 'thread': 348}**:
```json
{u'code': 0, u'response': {u'thread': 348, u'user': u'example3@mail.ru'}}
```
