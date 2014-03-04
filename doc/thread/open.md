#Thread.open
Mark thread as opened

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/open/ with _{'thread': 256}_:
```json
{u'code': 0, u'response': {u'thread': 256}}
```
