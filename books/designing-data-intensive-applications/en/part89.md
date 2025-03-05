### The relational model What the relational model did, by contrast, was to lay out all the data in the open: a relation
(table) is simply a collection of tuples (rows), and that’s it. There are no labyrinthine nested
structures, no complicated access paths to follow if you want to look at the data. You can read any
or all of the rows in a table, selecting those that match an arbitrary condition. You can read a
particular row by designating some columns as a key and matching on those. You can insert a new row
into any table without worrying about foreign key relationships to and from other
tables.[iv](ch02.html#idm140605782388832) 
In a relational database, the query optimizer automatically decides which parts of the query to
execute in which order, and which indexes to use. Those choices are effectively the “access path,”
but the big difference is that they are made automatically by the query optimizer, not by the
application developer, so we rarely need to think about them.