###### Note 
The word log is often used to refer to application logs, where an application outputs text that
describes what’s happening. In this book, log is used in the more general sense: an append-only
sequence of records. It doesn’t have to be human-readable; it might be binary and intended only for
other programs to read. On the other hand, our db_get function has terrible performance if you have a large number of
records in your database. Every time you want to look up a key, db_get has to scan the entire
database file from beginning to end, looking for occurrences of the key. In algorithmic terms, the
cost of a lookup is O(n): if you double the number of records n in your database, a lookup
takes twice as long. That’s not good. 
In order to efficiently find the value for a particular key in the database, we need a different
data structure: an index. In this chapter we will look at a range of indexing structures and see
how they compare; the general idea behind them is to keep some additional metadata on the side,
which acts as a signpost and helps you to locate the data you want. If you want to search the same
data in several different ways, you may need several different indexes on different parts of the
data.