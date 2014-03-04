#User.follow
Mark one user as folowing other user

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* follower

   ```str``` follower email
* followee

   ```str``` followee email


Requesting http://some.host.ru/db/api/s.stupnikov/user/follow/ with **{'follower': 'example@mail.ru', 'followee': 'example3@mail.ru'}**:
```json
{u'code': 0,
 u'response': {u'about': u'hello im user1',
               u'email': u'example@mail.ru',
               u'followers': [u'example3@mail.ru'],
               u'following': [u'example3@mail.ru'],
               u'id': 791,
               u'isAnonymous': False,
               u'name': u'John',
               u'subscriptions': [297],
               u'username': u'user1'}}
```
