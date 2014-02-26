#Forum.create

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional

###Requried
* user
* short_name
* name

Requesting http://some.host.ru/db/api/s.stupnikov/forum/create/ with _{'name': 'Forum With Sufficiently Large Name', 'short_name': 'forumwithsufficientlylargename', 'user': 'richard.nixon@example.com'}_:
```json
{u'code': 0,
 u'response': {u'id': 958,
               u'name': u'Forum With Sufficiently Large Name',
               u'short_name': u'forumwithsufficientlylargename',
               u'user': u'richard.nixon@example.com'}}
```
