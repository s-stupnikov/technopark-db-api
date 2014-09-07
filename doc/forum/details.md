#Forum.details
Get forum details

## Supported request methods 
* GET

##Arguments
###Optional
* related

   ```array``` include related entities. Possible values: ```['user',]```. Default: []


###Requried
* forum

   ```str``` forum short_name


Requesting http://some.host.ru/db/api/forum/details/?related=user&forum=forum3:
```json
{
    "code": 0,
    "response": {
        "id": 4,
        "name": "\u0424\u043e\u0440\u0443\u043c \u0422\u0440\u0438",
        "short_name": "forum3",
        "user": {
            "about": "hello im user2",
            "email": "example2@mail.ru",
            "followers": [],
            "following": [],
            "id": 3,
            "isAnonymous": false,
            "name": "Jey",
            "subscriptions": [],
            "username": "user2"
        }
    }
}
```
