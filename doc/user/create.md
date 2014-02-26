#User.create

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional
* isAnonymous

###Requried
* name
* email

Requesting http://some.host.ru/db/api/s.stupnikov/user/create/ with _{'username': 'user1', 'about': 'hello im user1', 'isAnonymous': False, 'name': 'John', 'email': 'example@mail.ru'}_:
```json
{u'code': 0,
 u'response': {u'about': u'hello im user1',
               u'email': u'example@mail.ru',
               u'id': 390,
               u'isAnonymous': False,
               u'name': u'John',
               u'username': u'user1'}}
```
