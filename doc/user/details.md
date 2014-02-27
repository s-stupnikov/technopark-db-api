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


Requesting http://some.host.ru/db/api/s.stupnikov/user/details/ with _{'user': 'example3@mail.ru'}_:
```json
{u'code': 0,
 u'response': {u'about': u'Wowowowow!!!',
               u'email': u'example3@mail.ru',
               u'followers': [u'example@mail.ru'],
               u'following': [u'example@mail.ru'],
               u'id': 726,
               u'isAnonymous': False,
               u'name': u'NewName2',
               u'subscriptions': [358],
               u'username': u'user3'}}
```
