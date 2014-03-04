#Thread.create
Create new thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional
* isDeleted

   ```bool``` is thread marked as deleted


###Requried
* forum

   ```str``` parent forum short_name
* title

   ```str``` thread title
* isClosed

   ```bool``` is thread marked as closed
* user

   ```str``` founder email
* date

   ```str``` date of creation. Format: 'YYYY-MM-DD hh-mm-ss'
* message

   ```str``` thread message
* slug

   ```str``` thread slug


Requesting http://some.host.ru/db/api/s.stupnikov/thread/create/ with **{'forum': 'forum3', 'title': 'Thread With Sufficiently Large Title', 'isClosed': True, 'user': 'example4@mail.ru', 'date': '2014-01-01 00:00:01', 'message': 'hey hey hey hey!', 'slug': 'Threadwithsufficientlylargetitle', 'isDeleted': True}**:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'forum': u'forum3',
               u'id': 78,
               u'isClosed': True,
               u'isDeleted': True,
               u'message': u'hey hey hey hey!',
               u'slug': u'Threadwithsufficientlylargetitle',
               u'title': u'Thread With Sufficiently Large Title',
               u'user': u'example4@mail.ru'}}
```
