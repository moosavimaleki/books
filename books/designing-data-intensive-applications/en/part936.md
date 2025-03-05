
Kafka Connect [[41](ch11.html#Narkhede2016uo)] is an effort to integrate change data capture tools for a wide range of
database systems with Kafka. Once the stream of change events is in Kafka, it can be used to update
derived data systems such as search indexes, and also feed into stream processing systems as
discussed later in this chapter. ## Event Sourcing 
There are some parallels between the ideas we’ve discussed here and event sourcing, a technique
that was developed in the domain-driven design (DDD) community
[[42](ch11.html#Young2014wp), [43](ch11.html#Fowler2005vd), [44](ch11.html#Vernon2013ww)]. We will discuss event
sourcing briefly, because it incorporates some useful and relevant ideas for streaming systems. 
Similarly to change data capture, event sourcing involves storing all changes to the application
state as a log of change events. The biggest difference is that event sourcing applies the idea at a
different level of abstraction: *  In change data capture, the application uses the database in a mutable way, updating and deleting
records at will. The log of changes is extracted from the database at a low level (e.g., by parsing
the replication log), which ensures that the order of writes extracted from the database matches
the order in which they were actually written, avoiding the race condition in
[Figure 11-4](#fig_stream_write_order). The application writing to the database does not need to be aware that
CDC is occurring.