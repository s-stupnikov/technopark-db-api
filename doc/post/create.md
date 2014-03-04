#Post.create
Create new post

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional
* isHighlighted

   ```bool``` is post marked as higlighted
* isApproved

   ```bool``` is post marked as approved by moderator
* isSpam

   ```bool``` is post marked as spam
* isDeleted

   ```bool``` is post marked as deleted
* isEdited

   ```bool``` is post marked as edited


###Requried
* parent

   ```int``` id of parent post
* forum

   ```str``` forum short_name
* thread

   ```int``` thread id of this post
* user

   ```str``` author email
* date

   ```str``` date of creation. Format: 'YYYY-MM-DD hh-mm-ss'
* message

   ```str``` post body


Requesting http://some.host.ru/db/api/s.stupnikov/post/create/ with ```{'isApproved': True, 'user': 'richard.nixon@example.com', 'date': '2014-01-01 00:00:01', 'message': 'my message 1', 'isSpam': False, 'isHighlighted': True, 'thread': 311, 'forum': 'forum3', 'isDeleted': False, 'isEdited': True}```:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'forum': u'forum3',
               u'id': 243,
               u'isApproved': True,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': True,
               u'isSpam': False,
               u'message': u'my message 1',
               u'thread': 311,
               u'user': u'richard.nixon@example.com'}}
```
