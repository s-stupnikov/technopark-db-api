#User.unfollow
Mark one user as not folowing other user anymore

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


Requesting http://some.host.ru/db/api/s.stupnikov/user/unfollow/ with **{'follower': 'example@mail.ru', 'followee': 'example3@mail.ru'}**:
```json
{u'code': 0,
 u'response': {u'about': u'hello im user1',
               u'email': u'example@mail.ru',
               u'followers': [],
               u'following': [],
               u'id': 791,
               u'isAnonymous': False,
               u'name': u'John',
               u'subscriptions': [297],
               u'username': u'user1'}}
```
