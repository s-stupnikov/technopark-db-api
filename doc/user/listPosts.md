#User.listPosts
Get posts from this user

## Supported request methods 
* GET

##Arguments
###Optional
* since

   ```str``` include posts from this user created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit

* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user

   ```str``` user email


Requesting http://some.host.ru/db/api/user/listPosts/?since=2014-01-02+00%3A00%3A00&limit=2&user=example%40mail.ru&order=asc:
```json
{
    "code": 0,
    "response": [
        {
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
