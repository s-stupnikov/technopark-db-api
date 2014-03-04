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


Requesting http://some.host.ru/db/api/s.stupnikov/user/updateProfile/ with ```{'about': 'Wowowowow!!!', 'user': 'example3@mail.ru', 'name': 'NewName2'}```:
```json
{u'code': 0,
 u'response': {u'about': u'Wowowowow!!!',
               u'email': u'example3@mail.ru',
               u'followers': [],
               u'following': [],
               u'id': 58,
               u'isAnonymous': False,
               u'name': u'NewName2',
               u'subscriptions': [681],
               u'username': u'user3'}}
```
