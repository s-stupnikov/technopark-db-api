#Post.restore
Cancel removal

## Supported request methods 
* POST

##Supported formats
* json

##Arguments


###Requried
* post

   ```int``` post id


Requesting http://some.host.ru/db/api/post/restore/ with *{"post": 3}*:
```json
{
    "code": 0,
    "response": {
        "post": 3
    }
}
```
