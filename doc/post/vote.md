#Post.vote
like/dislike post

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* vote

   ```int``` like/dislike. Possible values: [1, -1]
* post

   ```int``` post id


Requesting http://some.host.ru/db/api/post/vote/ with *{"vote": -1, "post": 5}*:
```json
{
    "code": 0,
    "response": {
        "date": "2014-01-03 00:08:01",
        "dislikes": 1,
        "forum": "forum1",
        "id": 5,
        "isApproved": false,
        "isDeleted": true,
        "isEdited": false,
        "isHighlighted": false,
        "isSpam": false,
        "likes": 0,
        "message": "my message 1",
        "parent": null,
        "points": -1,
        "thread": 3,
        "user": "richard.nixon@example.com"
    }
}
```
