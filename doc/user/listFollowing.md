#User.listFollowing
Get followees of this user

## Supported request methods 
* GET

##Arguments
###Optional
* limit

   ```int``` return limit
* order

   ```str``` sort order (by name). Possible values: ```['desc', 'asc']```. Default: 'desc'
* since_id

   ```int``` return entities in interval [since_id, max_id]


###Requried
* user

   ```str``` user email


Requesting http://some.host.ru/db/api/user/listFollowing/?limit=3&user=example3%40mail.ru&since_id=1&order=desc:
```json
{
    "code": 0,
    "response": [
        {
            "about": "hello im user1",
            "email": "example@mail.ru",
            "followers": [
                "example3@mail.ru"
            ],
            "following": [
                "example3@mail.ru"
            ],
            "id": 1,
            "isAnonymous": false,
            "name": "John",
            "subscriptions": [
                4
            ],
            "username": "user1"
        }
    ]
}
```
