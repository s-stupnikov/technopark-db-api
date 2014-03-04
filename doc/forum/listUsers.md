#Forum.listUsers
Get user with posts on this forum

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* limit

   ```int``` return limit
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'
* since_id

   ```int``` return entities in interval [since_id, max_id]


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listUsers/ with ```{'limit': 2, 'since_id': 10, 'forum': 'forumwithsufficientlylargename', 'order': 'asc'}```:
```json
{u'code': 0, u'response': []}
```
