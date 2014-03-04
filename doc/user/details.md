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


Requesting http://some.host.ru/db/api/s.stupnikov/user/details/ with **{'user': 'example@mail.ru'}**:
```json
{u'code': 0,
 u'response': {u'about': u'hello im user1',
               u'email': u'example@mail.ru',
               u'followers': [u'example3@mail.ru'],
               u'following': [u'example3@mail.ru'],
               u'id': 943,
               u'isAnonymous': False,
               u'name': u'John',
               u'subscriptions': [709, 560],
               u'username': u'user1'}}
```
