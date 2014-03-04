#User.details
Get user details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments


###Requried
* user

   ```str``` user email


Requesting http://some.host.ru/db/api/s.stupnikov/user/details/ with _{'user': 'example@mail.ru'}_:
```json
{u'code': 0,
 u'response': {u'about': u'hello im user1',
               u'email': u'example@mail.ru',
               u'followers': [u'example3@mail.ru'],
               u'following': [u'example3@mail.ru'],
               u'id': 988,
               u'isAnonymous': False,
               u'name': u'John',
               u'subscriptions': [256],
               u'username': u'user1'}}
```
