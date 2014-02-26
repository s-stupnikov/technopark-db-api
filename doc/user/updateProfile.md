#User.updateProfile

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional

###Requried
* user
* name
* about

Requesting http://some.host.ru/db/api/s.stupnikov/user/updateProfile/ with _{'about': 'Wowowowow', 'user': 'example2@mail.ru', 'name': 'NewName'}_:
```json
{u'code': 0,
 u'response': {u'about': u'Wowowowow',
               u'email': u'example2@mail.ru',
               u'followers': [],
               u'following': [],
               u'id': 14,
               u'isAnonymous': False,
               u'name': u'NewName',
               u'subscriptions': [182],
               u'username': u'user2'}}
```
