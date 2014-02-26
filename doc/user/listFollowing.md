#User.listFollowing

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order

###Requried
* user

Requesting http://some.host.ru/db/api/s.stupnikov/user/listFollowing/ with _{'limit': 3, 'user': 'example3@mail.ru', 'since_id': 1, 'order': 'desc'}_:
```json
{u'code': 0,
 u'response': [{u'about': u'hello im user1',
                u'email': u'example@mail.ru',
                u'followers': [u'example3@mail.ru'],
                u'following': [u'example3@mail.ru'],
                u'id': 390,
                u'isAnonymous': False,
                u'name': u'John',
                u'subscriptions': [],
                u'username': u'user1'}]}
```
