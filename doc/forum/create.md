#Forum.create
Create new forum

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* name

   ```str``` forum name
* short_name

   ```str``` forum slug
* user

   ```str``` founder email


Requesting http://some.host.ru/db/api/s.stupnikov/forum/create/ with **{'name': 'Forum With Sufficiently Large Name', 'short_name': 'forumwithsufficientlylargename', 'user': 'example@mail.ru'}**:
```json
{u'code': 0,
 u'response': {u'id': 39,
               u'name': u'Forum With Sufficiently Large Name',
               u'short_name': u'forumwithsufficientlylargename',
               u'user': u'example@mail.ru'}}
```
