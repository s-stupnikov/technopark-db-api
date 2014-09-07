#Post.remove
Mark post as removed

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* post

   ```int``` post id


Requesting http://some.host.ru/db/api/post/remove/ with *{"post": 3}*:
```json
{
    "code": 0,
    "response": {
        "post": 3
    }
}
```
