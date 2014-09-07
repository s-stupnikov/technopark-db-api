#Forum.listUsers
Get user with posts on this forum

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
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/forum/listUsers/?order=desc&forum=forum1:
```json
{
    "code": 0,
    "response": [
        {
            "about": null,
            "email": "richard.nixon@example.com",
            "followers": [],
            "following": [],
            "id": 2,
            "isAnonymous": true,
            "name": null,
            "subscriptions": [],
            "username": null
        },
        {
            "about": "hello im user1",
            "email": "example@mail.ru",
            "followers": [],
            "following": [],
            "id": 1,
            "isAnonymous": false,
            "name": "John",
            "subscriptions": [],
            "username": "user1"
        }
    ]
}
```
