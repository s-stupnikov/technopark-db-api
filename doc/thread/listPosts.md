#Thread.listPosts
Get posts from this thread

## Supported request methods 
* GET

##Arguments
###Optional
* since

   ```str``` include threads created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* limit

   ```int``` return limit
* sort
  
   ```str``` sort type. Possible values: ```['flat', 'tree', 'parent_tree']```. Default: 'flat'
* order

   ```str``` sort order. Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/thread/listPosts/?since=2014-01-02+00%3A00%3A00&limit=2&order=asc&thread=3:
```json
{
    "code": 0,
    "response": [
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
        },
        {
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
    ]
}
```
