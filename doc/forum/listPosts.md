#Forum.listPosts

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

Requesting http://some.host.ru/db/api/s.stupnikov/forum/listPosts/ with _{'related': ['thread'], 'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'forum': 'forumwithsufficientlylargename'}_:
```json
{u'code': 0, u'response': []}
```
