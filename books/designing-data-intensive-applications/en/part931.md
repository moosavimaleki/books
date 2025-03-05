Essentially, change data capture makes one database the leader (the one from which the changes are
captured), and turns the others into followers. A log-based message broker is well suited for
transporting the change events from the source database, since it preserves the ordering of messages
(avoiding the reordering issue of [Figure 11-2](#fig_stream_redelivery)). 
Database triggers can be used to implement change data capture (see [“Trigger-based replication”](ch05.html#sec_replication_trigger)) by
registering triggers that observe all changes to data tables and add corresponding entries to a
changelog table.  However, they tend to be fragile and have significant performance overheads.
Parsing the replication log can be a more robust approach, although it also comes with challenges,
such as handling schema changes. 
LinkedIn’s Databus
[[25](ch11.html#Das2012uf_ch11)], Facebook’s Wormhole
[[26](ch11.html#Sharma2015te_ch11)], and Yahoo!’s Sherpa
[[27](ch11.html#Narayan2010wq)] use this idea at large
scale. Bottled Water implements CDC for PostgreSQL using an API that decodes the write-ahead log
[[28](ch11.html#Kleppmann2015vl)],
Maxwell and Debezium do something similar for MySQL by parsing the binlog
[[29](ch11.html#Osheroff2015uy),
[30](ch11.html#Debezium2016), [31](ch11.html#Shankar2016ug)],
Mongoriver reads the MongoDB oplog
[[32](ch11.html#Mongoriver2016), [33](ch11.html#Harvey2015vl)],
and GoldenGate provides similar facilities for Oracle
[[34](ch11.html#GoldenGate2013ub),
[35](ch11.html#GoldenGate2012ct)].