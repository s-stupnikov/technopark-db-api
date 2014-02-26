#User.listPosts

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order
* since

###Requried
* user

Requesting http://some.host.ru/db/api/s.stupnikov/user/listPosts/ with _{'since': '2014-01-02 00:00:00', 'limit': 2, 'user': 'example@mail.ru', 'order': 'asc'}_:
```json
{u'code': 0, u'response': []}
```
