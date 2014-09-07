#Thread.unsubscribe
Unsubscribe user from this thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* user

   ```str``` founder email
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/thread/unsubscribe/ with *{"user": "example4@mail.ru", "thread": 1}*:
```json
{
    "code": 0,
    "response": {
        "thread": 1,
        "user": "example4@mail.ru"
    }
}
```
