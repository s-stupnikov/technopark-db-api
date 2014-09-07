#User.updateProfile
Update profile

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* about

   ```str``` user info
* user

   ```str``` user email
* name

   ```str``` user name


Requesting http://some.host.ru/db/api/user/updateProfile/ with *{"about": "Wowowowow!!!", "user": "example3@mail.ru", "name": "NewName2"}*:
```json
{
    "code": 0,
    "response": {
        "about": "Wowowowow!!!",
        "email": "example3@mail.ru",
        "followers": [],
        "following": [],
        "id": 4,
        "isAnonymous": false,
        "name": "NewName2",
        "subscriptions": [
            3,
            1
        ],
        "username": "user3"
    }
}
```
