#User.listFollowers

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order
###Requried
* user

Requesting http://some.host.ru/db/api/s.stupnikov/user/listFollowers/ with _{'limit': 3, 'user': 'example3@mail.ru', 'since_id': 2, 'order': 'desc'}_:
```json
{u'code': 0,
 u'response': [{u'about': u'hello im user1',
                u'email': u'example@mail.ru',
                u'followers': [u'example3@mail.ru'],
                u'following': [u'example3@mail.ru'],
                u'id': 321,
                u'isAnonymous': False,
                u'name': u'John',
                u'subscriptions': [182],
                u'username': u'user1'}]}
```
