The problem with the mod N approach is that if the number of nodes N changes, most of the keys
will need to be moved from one node to another. For example, say hash(key) = 123456.  If you
initially have 10 nodes, that key starts out on node 6
(because 123456 mod 10 = 6). When you grow to 11 nodes, the key needs to
move to node 3 (123456 mod 11 = 3), and when you grow to 12 nodes, it needs
to move to node 0 (123456 mod 12 = 0). Such frequent moves make rebalancing
excessively expensive. We need an approach that doesn’t move data around more than necessary. ### Fixed number of partitions 
Fortunately, there is a fairly simple solution: create many more partitions than there are nodes,
and assign several partitions to each node. For example, a database running on a cluster of 10 nodes
may be split into 1,000 partitions from the outset so that approximately 100 partitions are
assigned to each node.