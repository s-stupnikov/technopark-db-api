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
* isEdited

   ```bool``` is post marked as edited
* isSpam

   ```bool``` is post marked as spam
* isDeleted

   ```bool``` is post marked as deleted
* isApproved

   ```bool``` is post marked as approved by moderator


###Requried
* date

   ```str``` date of creation. Format: 'YYYY-MM-DD hh-mm-ss'
* message

   ```str``` post body
* thread

   ```int``` thread id of this post
* forum

   ```str``` forum short_name
* user

   ```str``` author email


Requesting http://some.host.ru/db/api/s.stupnikov/post/create/ with _{'isApproved': True, 'user': 'example4@mail.ru', 'date': '2014-01-01 00:00:01', 'message': 'my message 1', 'isSpam': False, 'isHighlighted': True, 'thread': 541, 'forum': 'forumwithsufficientlylargename', 'isDeleted': False, 'isEdited': True}_:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'forum': u'forumwithsufficientlylargename',
               u'id': 304,
               u'isApproved': True,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': True,
               u'isSpam': False,
               u'message': u'my message 1',
               u'thread': 541,
               u'user': u'example4@mail.ru'}}
```
