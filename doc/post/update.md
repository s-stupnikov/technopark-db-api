#Post.update
Edit post

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* post

   ```int``` post id
* message

   ```str``` post body


Requesting http://some.host.ru/db/api/post/update/ with *{"post": 3, "message": "my message 1"}*:
```json
{
    "code": 0,
    "response": {
        "date": "2014-01-02 00:02:01",
        "dislikes": 0,
        "forum": "forum2",
        "id": 3,
        "isApproved": false,
        "isDeleted": false,
        "isEdited": true,
        "isHighlighted": false,
        "isSpam": true,
        "likes": 0,
        "message": "my message 1",
        "parent": 2,
        "points": 0,
        "thread": 4,
        "user": "example@mail.ru"
    }
}
```
