#Forum.create
Create new forum

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* name

   ```str``` forum name
* short_name

   ```str``` forum slug
* user

   ```str``` founder email


Requesting http://some.host.ru/db/api/forum/create/ with *{"name": "Forum With Sufficiently Large Name", "short_name": "forumwithsufficientlylargename", "user": "richard.nixon@example.com"}*:
```json
{
    "code": 0,
    "response": {
        "id": 1,
        "name": "Forum With Sufficiently Large Name",
        "short_name": "forumwithsufficientlylargename",
        "user": "richard.nixon@example.com"
    }
}
```
