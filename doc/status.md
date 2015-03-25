#Status
Show status info: maps table name to number of rows in that table

## Supported request methods 
* GET

##Supported formats
* json

##Arguments

Requesting http://some.host.ru/db/api/status/ :
```json
{"code": 0, "response": {"user": 100000, "thread": 1000, "forum": 100, "post": 1000000}}
```
