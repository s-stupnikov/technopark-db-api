#Thread.list
List threads

## Supported request methods 
* GET

##Arguments
###Optional
* since

   ```str``` include threads created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user

   ```str``` founder email

OR
* forum

   ```str``` parent forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/thread/list/ with **{'since': '2014-01-01 00:00:00', 'user': 'example2@mail.ru', 'order': 'desc'}**:
```json
{u'code': 0,
 u'response': [{u'date': u'2014-01-01 00:00:01',
                u'dislikes': 0,
                u'forum': u'forumwithsufficientlylargename',
                u'id': 504,
                u'isClosed': True,
                u'isDeleted': True,
                u'likes': 0,
                u'message': u'hey hey hey hey!',
                u'points': 0,
                u'posts': 0,
                u'slug': u'Threadwithsufficientlylargetitle',
                u'title': u'Thread With Sufficiently Large Title',
                u'user': u'example2@mail.ru'}]}
```
