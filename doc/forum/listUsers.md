#Forum.listUsers

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order

###Requried
* forum

Requesting http://some.host.ru/db/api/s.stupnikov/forum/listUsers/ with _{'limit': 2, 'since_id': 10, 'forum': 'forumwithsufficientlylargename', 'order': 'asc'}_:
```json
{u'code': 0, u'response': []}
```
