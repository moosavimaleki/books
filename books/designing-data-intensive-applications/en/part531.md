[iv](ch07.html#idm140605774682240-marker) Strictly speaking, the term atomic
increment uses the word atomic in the sense of multi-threaded programming. In the
context of ACID, it should actually be called isolated or serializable increment.
But that’s getting nitpicky. [v](ch07.html#idm140605774566176-marker) Some databases support an even
weaker isolation level called read uncommitted. It prevents dirty writes, but does not
prevent dirty reads. [vi](ch07.html#idm140605774512368-marker) At the time of
writing, the only mainstream databases that use locks for read committed isolation are IBM
DB2 and Microsoft SQL Server in the read_committed_snapshot=off configuration
[[23](ch07.html#Kleppmann2014ut),
[36](ch07.html#Mukherjee2013uw)]. [vii](ch07.html#idm140605762226000-marker) To be precise, transaction IDs
are 32-bit integers, so they overflow after approximately 4 billion transactions. PostgreSQL’s
vacuum process performs cleanup which ensures that overflow does not affect the data. [viii](ch07.html#idm140605762119856-marker) It is possible, albeit fairly
complicated, to express the editing of a text document as a stream of atomic mutations. See
[“Automatic Conflict Resolution”](ch05.html#sidebar_conflict_resolution) for some pointers. [ix](ch07.html#idm140605761767776-marker) In
PostgreSQL you can do this more elegantly using range types, but they are not widely supported in
other databases.