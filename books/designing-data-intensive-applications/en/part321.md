
A trigger lets you register custom application code that is automatically executed when a data
change (write transaction) occurs in a database system. The trigger has the opportunity to log this
change into a separate table, from which it can be read by an external process. That external
process can then apply any necessary application logic and replicate the data change to another
system. Databus for Oracle
[[20](ch05.html#Das2012uf_ch5)]
and Bucardo for Postgres [[21](ch05.html#Mullane2014uy)]
work like this, for example. Trigger-based replication typically has greater overheads than other replication methods, and is
more prone to bugs and limitations than the database’s built-in replication. However, it can
nevertheless be useful due to its flexibility. # Problems with Replication Lag 
Being able to tolerate node failures is just one reason for wanting replication. As mentioned
in the introduction to [Part II](part02.html#part_distributed_data), other reasons are scalability (processing more
requests than a single machine can handle) and latency (placing replicas geographically closer to
users).