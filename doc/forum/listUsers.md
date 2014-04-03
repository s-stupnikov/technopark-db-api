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

   ```str``` sort order (by id). Possible values: ```['desc', 'asc']```. Default: 'desc'
* since_id

   ```int``` return entities in interval [since_id, max_id]


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listUsers/ with **{'limit': 2, 'since_id': 10, 'forum': 'forumwithsufficientlylargename', 'order': 'asc'}**:
```json
{u'code': 0,
 u'response': [{u'email': u'richard.nixon@example.com',
                u'followers': [],
                u'following': [],
                u'id': 121,
                u'isAnonymous': True,
                u'name': None,
                u'username': None,
                u'about': None,
                u'subscriptions': []},
               {u'about': u'hello im user2',
                u'email': u'example2@mail.ru',
                u'followers': [],
                u'following': [],
                u'id': 508,
                u'isAnonymous': False,
                u'name': u'Jey',
                u'subscriptions': [],
                u'username': u'user2'}]}
```
