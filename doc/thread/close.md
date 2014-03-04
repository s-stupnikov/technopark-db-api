#Thread.close
Mark thread as closed

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/s.stupnikov/thread/close/ with **{'thread': 709}**:
```json
{u'code': 0, u'response': {u'thread': 709}}
```
