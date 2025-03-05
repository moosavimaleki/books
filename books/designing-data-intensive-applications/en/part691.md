### Noncausal sequence number generators 
If there is not a single leader (perhaps because you are using a multi-leader or leaderless
database, or because the database is partitioned), it is less clear how to generate sequence numbers
for operations. Various methods are used in practice: *  Each node can generate its own independent set of sequence numbers. For example, if you have two
nodes, one node can generate only odd numbers and the other only even numbers. In general, you
could reserve some bits in the binary representation of the sequence number to contain a unique
node identifier, and this would ensure that two different nodes can never generate the same
sequence number. *  You can attach a timestamp from a time-of-day clock (physical clock) to each
operation [[55](ch09.html#Conery2014ti)]. Such timestamps are
not sequential, but if they have sufficiently high resolution, they might be sufficient to totally
order operations. This fact is used in the last write wins conflict resolution method (see
[“Timestamps for ordering events”](ch08.html#sec_distributed_lww)).