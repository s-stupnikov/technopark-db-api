#Thread.vote
like/dislike thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* vote

   ```int``` like/dislike. Possible values: [1, -1]
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/thread/vote/ with *{"vote": 1, "thread": 1}*:
```json
{
    "code": 0,
    "response": {
        "date": "2014-01-01 00:00:01",
        "dislikes": 0,
        "forum": "forum1",
        "id": 1,
        "isClosed": false,
        "isDeleted": false,
        "likes": 1,
        "message": "hey hey hey hey!",
        "points": 1,
        "posts": 0,
        "slug": "newslug",
        "title": "Thread With Sufficiently Large Title",
        "user": "example3@mail.ru"
    }
}
```
