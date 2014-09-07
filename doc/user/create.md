#User.create
Create new user

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional
* isAnonymous

   ```bool``` is user marked as anonymous


###Requried
* username

   ```str``` user name
* about

   ```str``` user info
* name

   ```str``` user name
* email

   ```str``` user email


Requesting http://some.host.ru/db/api/user/create/ with *{"username": "user1", "about": "hello im user1", "isAnonymous": false, "name": "John", "email": "example@mail.ru"}*:
```json
{
    "code": 0,
    "response": {
        "about": "hello im user1",
        "email": "example@mail.ru",
        "id": 1,
        "isAnonymous": false,
        "name": "John",
        "username": "user1"
    }
}
```
