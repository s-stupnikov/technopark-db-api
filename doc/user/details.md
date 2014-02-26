#User.details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* related

###Requried
* user

Requesting http://some.host.ru/db/api/s.stupnikov/user/details/ with _{'user': 'example@mail.ru', 'related': []}_:
```json
{u'code': 0,
 u'response': {u'about': u'hello im user1',
               u'email': u'example@mail.ru',
               u'followers': [],
               u'following': [],
               u'id': 390,
               u'isAnonymous': False,
               u'name': u'John',
               u'subscriptions': [],
               u'username': u'user1'}}
```
