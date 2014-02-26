#Forum.listThreads

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order
* since

###Requried
* forum

Requesting http://some.host.ru/db/api/s.stupnikov/forum/listThreads/ with _{'related': ['forum', 'user'], 'since': '2013-12-30 00:00:00', 'limit': 2, 'order': 'asc', 'forum': 'forumwithsufficientlylargename'}_:
```json
{u'code': 0, u'response': []}
```
