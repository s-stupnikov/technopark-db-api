#Forum.listUsers

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order
###Requried
* forum

Requesting http://some.host.ru/db/api/s.stupnikov/forum/listUsers/ with _{'limit': 2, 'since_id': 10, 'forum': 'forumwithsufficientlylargename', 'order': 'asc'}_:
```json
{u'code': 0,
 u'response': [{u'about': u'hello im user4',
                u'email': u'example4@mail.ru',
                u'followers': [],
                u'following': [],
                u'id': 998,
                u'isAnonymous': False,
                u'name': u'Jim',
                u'subscriptions': [],
                u'username': u'user4'}]}
```
