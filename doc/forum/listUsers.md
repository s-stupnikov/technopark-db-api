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


Requesting http://some.host.ru/db/api/s.stupnikov/forum/listUsers/ with **{'order': 'desc', 'forum': 'forum1'}**:
```json
{u'code': 0,
 u'response': [{u'about': u'hello im user1',
                u'email': u'example@mail.ru',
                u'followers': [],
                u'following': [],
                u'id': 943,
                u'isAnonymous': False,
                u'name': u'John',
                u'subscriptions': [],
                u'username': u'user1'},
               {u'about': u'hello im user1',
                u'email': u'example@mail.ru',
                u'followers': [],
                u'following': [],
                u'id': 943,
                u'isAnonymous': False,
                u'name': u'John',
                u'subscriptions': [],
                u'username': u'user1'},
               {u'about': u'hello im user3',
                u'email': u'example3@mail.ru',
                u'followers': [],
                u'following': [],
                u'id': 344,
                u'isAnonymous': False,
                u'name': u'Josh',
                u'subscriptions': [],
                u'username': u'user3'}]}
```
