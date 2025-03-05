
A logical log format is also easier for external applications to parse. This aspect is useful if you want
to send the contents of a database to an external system, such as a data warehouse for offline
analysis, or for building custom indexes and caches
[[18](ch05.html#Sharma2015te_ch5)].
This technique is called change data capture, and we will return to it in [Chapter 11](ch11.html#ch_stream). ### Trigger-based replication 
The replication approaches described so far are implemented by the database system, without
involving any application code. In many cases, that’s what you want—but there are some
circumstances where more flexibility is needed. For example, if you want to only replicate a subset
of the data, or want to replicate from one kind of database
to another, or if you need conflict resolution logic (see [“Handling Write Conflicts”](#sec_replication_write_conflicts)), then
you may need to move replication up to the application layer. 
Some tools, such as Oracle GoldenGate
[[19](ch05.html#Oracle2013ub)],
can make data changes available to an application by reading the database log. An alternative is to use features that are available in
many relational databases: triggers and stored procedures.