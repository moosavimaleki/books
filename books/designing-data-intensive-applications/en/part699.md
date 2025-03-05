# Scope of ordering guarantee 
Partitioned databases with a single leader per partition often maintain ordering only per partition,
which means they cannot offer consistency guarantees (e.g., consistent snapshots, foreign key
references) across partitions. Total ordering across all partitions is possible, but requires
additional coordination [[59](ch09.html#Balakrishnan2012wm)]. 
Total order broadcast is usually described as a protocol for exchanging messages between nodes.
Informally, it requires that two safety properties always be satisfied: Reliable delivery No messages are lost: if a message is delivered to one node, it is delivered to all nodes. Totally ordered delivery Messages are delivered to every node in the same order. A correct algorithm for total order broadcast must ensure that the reliability and ordering
properties are always satisfied, even if a node or the network is faulty. Of course, messages will
not be delivered while the network is interrupted, but an algorithm can keep retrying so that the
messages get through when the network is eventually repaired (and then they must still be delivered
in the correct order).