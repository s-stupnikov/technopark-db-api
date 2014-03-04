#User.listPosts
Get posts from this user

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* since

   ```str``` include posts from this user created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit
* order

   ```str``` sort order (by name). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user

   ```str``` user email


Requesting http://some.host.ru/db/api/s.stupnikov/user/listPosts/ with _{'since': '2014-01-02 00:00:00', 'limit': 2, 'user': 'example@mail.ru', 'order': 'asc'}_:
```json
{u'code': 0, u'response': []}
```
