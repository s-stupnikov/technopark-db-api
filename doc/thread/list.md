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
* limit

   ```int``` return limit
* order

   ```str``` sort order (by date). Possible values: ```['desc', 'asc']```. Default: 'desc'


###Requried
* user

   ```str``` founder email
* forum

   ```str``` parent forum short_name


Requesting http://some.host.ru/db/api/s.stupnikov/thread/list/ with **{'since': '2014-01-02 00:00:00', 'limit': 2, 'order': 'asc', 'forum': 'forumwithsufficientlylargename'}**:
```json
{u'code': 0, u'response': []}
```
