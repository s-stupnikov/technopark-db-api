#Thread.subscribe
Subscribe user to this thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* user

   ```str``` subscriber email
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/thread/subscribe/ with *{"user": "richard.nixon@example.com", "thread": 4}*:
```json
{
    "code": 0,
    "response": {
        "thread": 4,
        "user": "richard.nixon@example.com"
    }
}
```
