We said previously that an event is a record of something that happened at some point in time. The
thing that happened may be a user action (e.g., typing a search query), or a sensor reading, but it
may also be a write to a database. The fact that something was written to a database is an event
that can be captured, stored, and processed. This observation suggests that the connection between
databases and streams runs deeper than just the physical storage of logs on disk—it is quite
fundamental. 
In fact, a replication log (see [“Implementation of Replication Logs”](ch05.html#sec_replication_implementation)) is a stream of database write
events, produced by the leader as it processes transactions. The followers apply that stream of
writes to their own copy of the database and thus end up with an accurate copy of the same data.
The events in the replication log describe the data changes that occurred.