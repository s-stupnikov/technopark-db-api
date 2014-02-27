#Forum.listUsers
Get user with posts on this forum

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order
   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* forum
   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listUsers/ with _{'limit': 2, 'since_id': 10, 'forum': 'forumwithsufficientlylargename', 'order': 'asc'}_:
```json
{u'code': 0, u'response': []}
```
