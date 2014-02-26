#Thread.subscribe

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional

###Requried
* user
* thread

Requesting http://some.host.ru/db/api/s.stupnikov/thread/subscribe/ with _{'user': 'example@mail.ru', 'thread': 182}_:
```json
{u'code': 0, u'response': {u'thread': 182, u'user': u'example@mail.ru'}}
```
