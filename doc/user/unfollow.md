#User.unfollow

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional


###Requried
* followee
* follower

Requesting http://some.host.ru/db/api/s.stupnikov/user/unfollow/ with _{'follower': 'example3@mail.ru', 'followee': 'example@mail.ru'}_:
```json
{u'code': 0,
 u'response': {u'about': u'Wowowowow!!!',
               u'email': u'example3@mail.ru',
               u'followers': [u'example@mail.ru'],
               u'following': [],
               u'id': 79,
               u'isAnonymous': False,
               u'name': u'NewName2',
               u'subscriptions': [544],
               u'username': u'user3'}}
```
