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


Requesting http://some.host.ru/db/api/post/create/ with *{"isApproved": true, "user": "example@mail.ru", "date": "2014-01-01 00:00:01", "message": "my message 1", "isSpam": false, "isHighlighted": true, "thread": 4, "forum": "forum2", "isDeleted": false, "isEdited": true}*:
```json
{
    "code": 0,
    "response": {
        "date": "2014-01-01 00:00:01",
        "forum": "forum2",
        "id": 1,
        "isApproved": true,
        "isDeleted": false,
        "isEdited": true,
        "isHighlighted": true,
        "isSpam": false,
        "message": "my message 1",
        "parent": null,
        "thread": 4,
        "user": "example@mail.ru"
    }
}
```
