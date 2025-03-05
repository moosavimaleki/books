### Deriving several views from the same event log 
Moreover, by separating mutable state from the immutable event log, you can derive several different
read-oriented representations from the same log of events. This works just like having multiple
consumers of a stream ([Figure 11-5](#fig_stream_change_capture)): for example, the analytic database Druid
ingests directly from Kafka using this approach [[55](ch11.html#Yang2015ui)],
Pistachio is a distributed key-value store that uses Kafka as a commit log
[[56](ch11.html#Li2015vm)],
and Kafka Connect sinks can export data from Kafka to various different databases and indexes
[[41](ch11.html#Narkhede2016uo)]. It would make sense for many other
storage and indexing systems, such as search servers, to similarly take their input from a
distributed log (see [“Keeping Systems in Sync”](#sec_stream_sync)). 
Having an explicit translation step from an event log to a database makes it easier to evolve your
application over time: if you want to introduce a new feature that presents your existing data in
some new way, you can use the event log to build a separate read-optimized view for the new feature,
and run it alongside the existing systems without having to modify them. Running old and new systems
side by side is often easier than performing a complicated schema migration in an existing system.
Once the old system is no longer needed, you can simply shut it down and reclaim its resources
[[47](ch11.html#Kleppmann2016ug),
[57](ch11.html#Paramasivam2016th)].