#User.listFollowers
Get followers of this user

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


Requesting http://some.host.ru/db/api/s.stupnikov/user/listFollowers/ with _{'limit': 3, 'user': 'example3@mail.ru', 'since_id': 2, 'order': 'desc'}_:
```json
{u'code': 0,
 u'response': [{u'about': u'hello im user1',
                u'email': u'example@mail.ru',
                u'followers': [u'example3@mail.ru'],
                u'following': [u'example3@mail.ru'],
                u'id': 588,
                u'isAnonymous': False,
                u'name': u'John',
                u'subscriptions': [768],
                u'username': u'user1'}]}
```
