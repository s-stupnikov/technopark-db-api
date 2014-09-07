#Post.details
Get post details

## Supported request methods 
* GET

##Arguments
###Optional
* related

   ```array``` include related entities. Possible values: ```['user', 'thread', 'forum']```. Default: []


###Requried
* post

   ```int``` post id


Requesting http://some.host.ru/db/api/post/details/?post=3:
```json
{
    "code": 0,
    "response": {
        "date": "2014-01-02 00:02:01",
        "dislikes": 0,
        "forum": "forum2",
        "id": 3,
        "isApproved": false,
        "isDeleted": true,
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
