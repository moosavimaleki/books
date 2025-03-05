The situation would be better if there really was only one leader—for example, the database—and if
we could make the search index a follower of the database. But is this possible in practice? ## Change Data Capture 
The problem with most databases’ replication logs is that they have long been considered to be an
internal implementation detail of the database, not a public API. Clients are supposed to query the
database through its data model and query language, not parse the replication logs and try to
extract data from them. For decades, many databases simply did not have a documented way of getting the log of changes
written to them. For this reason it was difficult to take all the changes made in a database and
replicate them to a different storage technology such as a search index, cache, or data warehouse. 
More recently, there has been growing interest in change data capture (CDC), which is the process
of observing all data changes written to a database and extracting them in a form in which they can
be replicated to other systems. CDC is especially interesting if changes are made available as a
stream, immediately as they are written.