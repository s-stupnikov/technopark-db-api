#Forum.listPosts
Get posts from this forum

## Supported request methods 
* GET

##Arguments
###Optional
* since

   ```str``` include forums created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit

* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'
* related

   ```array``` include related entities. Possible values: ```['thread', 'forum', 'user']```. Default: []


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/forum/listPosts/?related=thread&related=forum&since=2014-01-01+00%3A00%3A00&order=desc&forum=forum1:
```json
{
    "code": 0,
    "response": [
        {
            "date": "2014-01-03 00:08:01",
            "dislikes": 0,
            "forum": {
                "id": 2,
                "name": "Forum I",
                "short_name": "forum1",
                "user": "example3@mail.ru"
            },
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
            "thread": {
                "date": "2013-12-30 00:01:01",
                "dislikes": 0,
                "forum": "forum1",
                "id": 3,
                "isClosed": false,
                "isDeleted": false,
                "likes": 0,
                "message": "hey hey!",
                "points": 0,
                "posts": 2,
                "slug": "thread2",
                "title": "Thread II",
                "user": "example3@mail.ru"
            },
            "user": "richard.nixon@example.com"
        },
        {
            "date": "2014-01-03 00:01:01",
            "dislikes": 0,
            "forum": {
                "id": 2,
                "name": "Forum I",
                "short_name": "forum1",
                "user": "example3@mail.ru"
            },
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
            "thread": {
                "date": "2013-12-30 00:01:01",
                "dislikes": 0,
                "forum": "forum1",
                "id": 3,
                "isClosed": false,
                "isDeleted": false,
                "likes": 0,
                "message": "hey hey!",
                "points": 0,
                "posts": 2,
                "slug": "thread2",
                "title": "Thread II",
                "user": "example3@mail.ru"
            },
            "user": "example@mail.ru"
        }
    ]
}
```
