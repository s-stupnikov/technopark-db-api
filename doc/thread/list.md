#Thread.list
List threads

## Supported request methods 
* GET

##Arguments
###Optional
* since

   ```str``` include threads created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user

   ```str``` founder email

OR
* forum

   ```str``` parent forum short_name


Requesting http://some.host.ru/db/api/thread/list/?since=2014-01-01+00%3A00%3A00&order=desc&forum=forum1:
```json
{
    "code": 0,
    "response": [
        {
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
    ]
}
```
