#User.listFollowers
Get followers of this user

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


Requesting http://some.host.ru/db/api/user/listFollowers/?user=example%40mail.ru&order=asc:
```json
{
    "code": 0,
    "response": [
        {
            "about": "Wowowowow!!!",
            "email": "example3@mail.ru",
            "followers": [
                "example@mail.ru"
            ],
            "following": [
                "example@mail.ru"
            ],
            "id": 4,
            "isAnonymous": false,
            "name": "NewName2",
            "subscriptions": [
                3,
                1
            ],
            "username": "user3"
        }
    ]
}
```
