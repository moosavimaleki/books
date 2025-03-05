
Like the version numbers in [Figure 5-13](#fig_replication_causality_single), version vectors are sent from the
database replicas to clients when values are read, and need to be sent back to the database when a
value is subsequently written. (Riak encodes the version vector as a string that it calls causal
context.) The version vector allows the database to distinguish between overwrites and concurrent
writes. Also, like in the single-replica example, the application may need to merge
siblings. The version vector structure ensures that it is safe to read from one replica and
subsequently write back to another replica. Doing so may result in siblings being created, but no data
is lost as long as siblings are merged correctly. # Version vectors and vector clocks 
A version vector is sometimes also called a vector clock, even though they are not quite the
same. The difference is subtle—please see the references for details
[[57](ch05.html#Preguica2010wu),
[60](ch05.html#Baquero2011ud),
[61](ch05.html#Schwarz1994gl)]. In brief, when
comparing the state of replicas, version vectors are the right data structure to use.