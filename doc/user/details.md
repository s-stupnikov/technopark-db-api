#User.details
Get user details

## Supported request methods 
* GET

##Arguments


###Requried
* user

   ```str``` user email


Requesting http://some.host.ru/db/api/user/details/?user=example%40mail.ru:
```json
{
    "code": 0,
    "response": {
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
}
```
