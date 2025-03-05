### API support for change streams 
Increasingly, databases are beginning to support change streams as a first-class interface, rather
than the typical retrofitted and reverse-engineered CDC efforts. For example, RethinkDB allows
queries to subscribe to notifications when the results of a query change
[[36](ch11.html#Akhmechet2015tq)], Firebase
[[37](ch11.html#Firebase2016)] and CouchDB
[[38](ch11.html#CouchDB2014_ch11)] provide data
synchronization based on a change feed that is also made available to applications, and Meteor uses
the MongoDB oplog to subscribe to data changes and update the user interface
[[39](ch11.html#DeBergalis2013vd)]. 
VoltDB allows transactions to continuously export data from a database in the form of a stream
[[40](ch11.html#VoltDBCh15)].
The database represents an output stream in the relational data model as a table into which
transactions can insert tuples, but which cannot be queried. The stream then consists of the log of
tuples that committed transactions have written to this special table, in the order they were
committed. External consumers can asynchronously consume this log and use it to update derived data
systems.