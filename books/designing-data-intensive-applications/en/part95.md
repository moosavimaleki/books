The difference between the approaches is particularly noticeable in situations where an application
wants to change the format of its data. For example, say you are currently storing each user’s full
name in one field, and you instead want to store the first name and last name separately
[[23](ch02.html#Irwin2013tb)].
In a document database, you would just start writing new documents with the new fields and have
code in the application that handles the case when old documents are read. For example: ```
`if` `(``user` `&&` `user``.``name` `&&` `!``user``.``first_name``)` `{`
    `// Documents written before Dec 8, 2013 don't have first_name`
    `user``.``first_name` `=` `user``.``name``.``split``(``" "``)[``0``];`
`}`
``` 
On the other hand, in a “statically typed” database schema, you would typically perform a
migration along the lines of: ```
`ALTER` `TABLE` `users` `ADD` `COLUMN` `first_name` `text``;`
`UPDATE` `users` `SET` `first_name` `=` `split_part``(``name``,` `' '``,` `1``);`      `-- PostgreSQL`
`UPDATE` `users` `SET` `first_name` `=` `substring_index``(``name``,` `' '``,` `1``);`      `-- MySQL`
```