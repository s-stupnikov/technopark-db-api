#Thread.listPosts

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* order
* since
###Requried
* thread

Requesting http://some.host.ru/db/api/s.stupnikov/thread/listPosts/ with _{'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'thread': 548}_:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-02 00:02:01',
                u'dislikes': 0,
                u'forum': u'forum1',
                u'id': 978,
                u'isApproved': False,
                u'isDeleted': False,
                u'isEdited': True,
                u'isHighlighted': False,
                u'isSpam': True,
                u'likes': 0,
                u'message': u'my message 1',
                u'parent': 362,
                u'points': 0,
                u'thread': 548,
                u'user': u'example@mail.ru'}]}
```
