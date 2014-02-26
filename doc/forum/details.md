#Forum.details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* related

###Requried
* forum

Requesting http://some.host.ru/db/api/s.stupnikov/forum/details/ with _{'related': [], 'forum': 'forumwithsufficientlylargename'}_:
```json
{u'code': 0,
 u'response': {u'id': 936,
               u'name': u'Forum With Sufficiently Large Name',
               u'short_name': u'forumwithsufficientlylargename',
               u'user': u'example@mail.ru'}}
```
