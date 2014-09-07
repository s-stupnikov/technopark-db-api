#Thread.restore
Cancel removal

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* thread

   ```int``` thread id of this post


Requesting http://some.host.ru/db/api/thread/restore/ with *{"thread": 1}*:
```json
{
    "code": 0,
    "response": {
        "thread": 1
    }
}
```
