#Thread.details
Get thread details

## Supported request methods 
* GET

##Arguments
###Optional
* related

   ```array``` include related entities. Possible values: ```['user', 'forum']```. Default: []


###Requried
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/thread/details/?thread=1:
```json
{
    "code": 0,
    "response": {
        "date": "2014-01-01 00:00:01",
        "dislikes": 0,
        "forum": "forum1",
        "id": 1,
        "isClosed": true,
        "isDeleted": true,
        "likes": 0,
        "message": "hey hey hey hey!",
        "points": 0,
        "posts": 0,
        "slug": "Threadwithsufficientlylargetitle",
        "title": "Thread With Sufficiently Large Title",
        "user": "example3@mail.ru"
    }
}
```
