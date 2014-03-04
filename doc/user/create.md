#User.create
Create new user

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional
* isAnonymous

   ```bool``` is user marked as anonymous


###Requried
* username

   ```str``` user name
* about

   ```str``` user info
* name

   ```str``` user name
* email

   ```str``` user email


Requesting http://some.host.ru/db/api/s.stupnikov/user/create/ with **{'username': 'user1', 'about': 'hello im user1', 'isAnonymous': False, 'name': 'John', 'email': 'example@mail.ru'}**:
```json
{u'code': 0,
 u'response': {u'about': u'hello im user1',
               u'email': u'example@mail.ru',
               u'id': 791,
               u'isAnonymous': False,
               u'name': u'John',
               u'username': u'user1'}}
```
