On the other hand, all-to-all topologies can have issues too. In particular, some network links may
be faster than others (e.g., due to network congestion), with the result that some replication
messages may “overtake” others, as illustrated in [Figure 5-9](#fig_replication_causality). ![ddia 0509](assets/ddia_0509.png) ###### Figure 5-9. With multi-leader replication, writes may arrive in the wrong order at some replicas. In [Figure 5-9](#fig_replication_causality), client A inserts a row into a table on leader 1, and client B
updates that row on leader 3. However, leader 2 may receive the writes in a different order: it may
first receive the update (which, from its point of view, is an update to a row that does not exist
in the database) and only later receive the corresponding insert (which should have preceded the
update). 
This is a problem of causality, similar to the one we saw in [“Consistent Prefix Reads”](#sec_replication_consistent_prefix):
the update depends on the prior insert, so we need to make sure that all nodes process the insert
first, and then the update. Simply attaching a timestamp to every write is not sufficient, because
clocks cannot be trusted to be sufficiently in sync to correctly order these events at leader 2 (see
[Chapter 8](ch08.html#ch_distributed)).