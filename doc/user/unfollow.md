#User.unfollow
Mark one user as not folowing other user anymore

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* follower

   ```str``` follower email
* followee

   ```str``` followee email


Requesting http://some.host.ru/db/api/user/unfollow/ with *{"follower": "example@mail.ru", "followee": "example3@mail.ru"}*:
```json
{
    "code": 0,
    "response": {
        "about": "hello im user1",
        "email": "example@mail.ru",
        "followers": [],
        "following": [],
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
