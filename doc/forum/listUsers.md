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

   ```int``` return forums in interval [since_id, max_id]


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listUsers/ with _{'limit': 2, 'since_id': 10, 'forum': 'forumwithsufficientlylargename', 'order': 'asc'}_:
```json
{u'code': 0,
 u'response': [{u'email': u'richard.nixon@example.com',
                u'followers': [],
                u'following': [],
                u'id': 26,
                u'isAnonymous': True,
                u'name': None,
                u'subscriptions': []},
               {u'about': u'hello im user3',
                u'email': u'example3@mail.ru',
                u'followers': [],
                u'following': [],
                u'id': 522,
                u'isAnonymous': False,
                u'name': u'Josh',
                u'subscriptions': [],
                u'username': u'user3'}]}
```
