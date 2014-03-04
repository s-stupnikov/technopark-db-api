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


###Requried
* since_id

   ```int``` return forums in interval [since_id, max_id]
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listUsers/ with _{'order': 'desc', 'forum': 'forum1'}_:
```json
{u'code': 0,
 u'response': [{u'email': u'richard.nixon@example.com',
                u'followers': [],
                u'following': [],
                u'id': 522,
                u'isAnonymous': True,
                u'name': None,
                u'subscriptions': []},
               {u'about': u'hello im user3',
                u'email': u'example3@mail.ru',
                u'followers': [],
                u'following': [],
                u'id': 489,
                u'isAnonymous': False,
                u'name': u'Josh',
                u'subscriptions': [],
                u'username': u'user3'},
               {u'about': u'hello im user3',
                u'email': u'example3@mail.ru',
                u'followers': [],
                u'following': [],
                u'id': 489,
                u'isAnonymous': False,
                u'name': u'Josh',
                u'subscriptions': [],
                u'username': u'user3'}]}
```
