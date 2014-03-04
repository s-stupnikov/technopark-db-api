#Post.create
Create new post

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional
* parent

   ```int``` id of parent post. Default: None
* isApproved

   ```bool``` is post marked as approved by moderator
* isHighlighted

   ```bool``` is post marked as higlighted
* isEdited

   ```bool``` is post marked as edited
* isSpam

   ```bool``` is post marked as spam
* isDeleted

   ```bool``` is post marked as deleted


###Requried
* date

   ```str``` date of creation. Format: 'YYYY-MM-DD hh-mm-ss'
* thread

   ```int``` thread id of this post
* message

   ```str``` post body
* user

   ```str``` author email
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/post/create/ with **{'isApproved': True, 'user': 'example2@mail.ru', 'date': '2014-01-01 00:00:01', 'message': 'my message 1', 'isSpam': False, 'isHighlighted': True, 'thread': 297, 'forum': 'forumwithsufficientlylargename', 'isDeleted': False, 'isEdited': True}**:
```json
{u'code': 0,
 u'response': {u'date': u'2014-01-01 00:00:01',
               u'forum': u'forumwithsufficientlylargename',
               u'id': 881,
               u'isApproved': True,
               u'isDeleted': False,
               u'isEdited': True,
               u'isHighlighted': True,
               u'isSpam': False,
               u'message': u'my message 1',
               u'thread': 297,
               u'user': u'example2@mail.ru'}}
```
