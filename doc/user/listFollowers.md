#User.listFollowers
Get followers of this user

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* limit

   ```int``` return limit
* order

   ```str``` sort order (by name). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user

   ```str``` user email
* since_id

   ```int``` return users in interval [since_id, max_id]


Requesting http://some.host.ru/db/api/s.stupnikov/user/listFollowers/ with _{'user': 'example@mail.ru', 'order': 'asc'}_:
```json
{u'code': 0,
 u'response': [{u'about': u'Wowowowow!!!',
                u'email': u'example3@mail.ru',
                u'followers': [u'example@mail.ru'],
                u'following': [u'example@mail.ru'],
                u'id': 489,
                u'isAnonymous': False,
                u'name': u'NewName2',
                u'subscriptions': [],
                u'username': u'user3'}]}
```
