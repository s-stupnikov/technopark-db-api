#Thread.create
Create new thread

## Supported request methods 
* POST

##Supported formats
* json

##Arguments
###Optional
* isDeleted

   ```bool``` is thread marked as deleted


###Requried
* forum

   ```str``` parent forum short_name
* title

   ```str``` thread title
* isClosed

   ```bool``` is thread marked as closed
* user

   ```str``` founder email
* date

   ```str``` date of creation. Format: 'YYYY-MM-DD hh-mm-ss'
* message

   ```str``` thread message
* slug

   ```str``` thread slug


Requesting http://some.host.ru/db/api/thread/create/ with *{"forum": "forum1", "title": "Thread With Sufficiently Large Title", "isClosed": true, "user": "example3@mail.ru", "date": "2014-01-01 00:00:01", "message": "hey hey hey hey!", "slug": "Threadwithsufficientlylargetitle", "isDeleted": true}*:
```json
{
    "code": 0,
    "response": {
        "date": "2014-01-01 00:00:01",
        "forum": "forum1",
        "id": 1,
        "isClosed": true,
        "isDeleted": true,
        "message": "hey hey hey hey!",
        "slug": "Threadwithsufficientlylargetitle",
        "title": "Thread With Sufficiently Large Title",
        "user": "example3@mail.ru"
    }
}
```
