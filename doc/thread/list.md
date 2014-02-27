#Thread.list
List threads

## Supported request methods 
* GET

##Supported formats
* json

##Arguments
###Optional
* since
   ```str``` include threads created since date. Format: 'YYYY-MM-DD hh-mm-ss'
* order
   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'




Requesting http://some.host.ru/db/api/s.stupnikov/thread/list/ with _{'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'forum': 'forumwithsufficientlylargename'}_:
```json
{u'code': 0, u'response': []}
```
