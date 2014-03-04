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


Requesting http://some.host.ru/db/api/s.stupnikov/thread/open/ with ```{'thread': 681}```:
```json
{u'code': 0, u'response': {u'thread': 681}}
```
