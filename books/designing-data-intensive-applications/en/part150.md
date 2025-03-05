And it works: ```

$ **db_set 123456 '{"name":"London","attractions":["Big Ben","London Eye"]}'**

$ **db_set 42 '{"name":"San Francisco","attractions":["Golden Gate Bridge"]}'**

$ **db_get 42**
{"name":"San Francisco","attractions":["Golden Gate Bridge"]} ``` 
The underlying storage format is very simple: a text file where each line contains a key-value pair,
separated by a comma (roughly like a CSV file, ignoring escaping issues). Every call to db_set
appends to the end of the file, so if you update a key several times, the old versions of the value
are not overwritten—you need to look at the last occurrence of a key in a file to find the latest
value (hence the tail -n 1 in db_get): ```

$ **db_set 42 '{"name":"San Francisco","attractions":["Exploratorium"]}'**

$ **db_get 42**
{"name":"San Francisco","attractions":["Exploratorium"]}

$ **cat database**
123456,{"name":"London","attractions":["Big Ben","London Eye"]}
42,{"name":"San Francisco","attractions":["Golden Gate Bridge"]}
42,{"name":"San Francisco","attractions":["Exploratorium"]} ``` 
Our db_set function actually has pretty good performance for something that is so simple, because
appending to a file is generally very efficient. Similarly to what db_set does, many databases
internally use a log, which is an append-only data file. Real databases have more issues to deal
with (such as concurrency control, reclaiming disk space so that the log doesn’t grow forever, and
handling errors and partially written records), but the basic principle is the same. Logs are
incredibly useful, and we will encounter them several times in the rest of this book.