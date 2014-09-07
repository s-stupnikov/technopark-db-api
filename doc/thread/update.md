#Thread.update
Edit thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* message

   ```str``` thread message
* slug

   ```str``` thread slug
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/thread/update/ with *{"message": "hey hey hey hey!", "slug": "newslug", "thread": 1}*:
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
        "likes": 0,
        "message": "hey hey hey hey!",
        "points": 0,
        "posts": 0,
        "slug": "newslug",
        "title": "Thread With Sufficiently Large Title",
        "user": "example3@mail.ru"
    }
}
```
