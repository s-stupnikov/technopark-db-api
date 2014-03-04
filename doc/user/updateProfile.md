#User.updateProfile
Update profile

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* about

   ```str``` user info
* user

   ```str``` user email
* name

   ```str``` user name


Requesting http://some.host.ru/db/api/s.stupnikov/user/updateProfile/ with _{'about': 'Wowowowow!!!', 'user': 'example3@mail.ru', 'name': 'NewName2'}_:
```json
{u'code': 0,
 u'response': {u'about': u'Wowowowow!!!',
               u'email': u'example3@mail.ru',
               u'followers': [],
               u'following': [],
               u'id': 522,
               u'isAnonymous': False,
               u'name': u'NewName2',
               u'subscriptions': [],
               u'username': u'user3'}}
```
