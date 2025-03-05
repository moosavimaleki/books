
Schema changes have a bad reputation of being slow and requiring downtime. This reputation is not
entirely deserved: most relational database systems execute the ALTER TABLE statement in a few
milliseconds. MySQL is a notable exception—it copies the entire table on ALTER TABLE, which
can mean minutes or even hours of downtime when altering a large table—although various tools exist to work
around this limitation [[24](ch02.html#Percona2013wb),
[25](ch02.html#Keddo2013vj),
[26](ch02.html#Noach2016bq)]. 
Running the UPDATE statement on a large table is likely to be slow on any database, since every
row needs to be rewritten. If that is not acceptable, the application can leave first_name set to
its default of NULL and fill it in at read time, like it would with a document database. The schema-on-read approach is advantageous if the items in the
collection don’t all have the same structure for some reason (i.e., the data is heterogeneous)—for example, because: *  There are many different types of objects, and it is not practical to put each type of object in
its own table.