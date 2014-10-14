#Post.list
List posts

## Supported request methods 
* GET

##Arguments
###Optional
* since

   ```str``` include posts created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit

* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* forum

   ```str``` forum short_name

OR
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/post/list/?since=2014-01-01+00%3A00%3A00&order=desc&forum=forum1:
```json
{
    "code": 0,
    "response": [
        {
            "date": "2014-01-03 00:08:01",
            "dislikes": 0,
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
            "points": 0,
            "thread": 3,
            "user": "richard.nixon@example.com"
        },
        {
            "date": "2014-01-03 00:01:01",
            "dislikes": 0,
            "forum": "forum1",
            "id": 4,
            "isApproved": true,
            "isDeleted": false,
            "isEdited": false,
            "isHighlighted": false,
            "isSpam": false,
            "likes": 0,
            "message": "my message 1",
            "parent": null,
            "points": 0,
            "thread": 3,
            "user": "example@mail.ru"
        }
    ]
}
```
