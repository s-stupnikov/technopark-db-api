#User.listFollowing
Get followees of this user

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order

   ```str``` sort order (by name). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user

   ```str``` user email


Requesting http://some.host.ru/db/api/s.stupnikov/user/listFollowing/ with _{'user': 'example@mail.ru', 'order': 'asc'}_:
```json
{u'code': 0,
 u'response': [{u'about': u'Wowowowow!!!',
                u'email': u'example3@mail.ru',
                u'followers': [u'example@mail.ru'],
                u'following': [u'example@mail.ru'],
                u'id': 726,
                u'isAnonymous': False,
                u'name': u'NewName2',
                u'subscriptions': [358],
                u'username': u'user3'}]}
```
