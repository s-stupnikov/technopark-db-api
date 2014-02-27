#Forum.details
Get forum details

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* related

   ```array``` include related entities. Possible values: ```['user',]```. Default: []


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/forum/details/ with _{'related': ['user'], 'forum': 'forum3'}_:
```json
{u'code': 0,
 u'response': {u'id': 819,
               u'name': u'\u0424\u043e\u0440\u0443\u043c \u0422\u0440\u0438',
               u'short_name': u'forum3',
               u'user': {u'about': u'hello im user3',
                         u'email': u'example3@mail.ru',
                         u'followers': [],
                         u'following': [],
                         u'id': 726,
                         u'isAnonymous': False,
                         u'name': u'Josh',
                         u'subscriptions': [],
                         u'username': u'user3'}}}
```
