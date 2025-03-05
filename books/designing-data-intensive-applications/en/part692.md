*  You can preallocate blocks of sequence numbers. For example, node A might claim the
block of sequence numbers from 1 to 1,000, and node B might claim the block from 1,001 to 2,000.
Then each node can independently assign sequence numbers from its block, and allocate a new block
when its supply of sequence numbers begins to run low. These three options all perform better and are more scalable than pushing all operations through a
single leader that increments a counter. They generate a unique, approximately increasing sequence
number for each operation. However, they all have a problem: the sequence numbers they generate are
not consistent with causality. The causality problems occur because these sequence number generators do not correctly capture the
ordering of operations across different nodes: *  Each node may process a different number of operations per second. Thus, if one node generates
even numbers and the other generates odd numbers, the counter for even numbers may lag behind the
counter for odd numbers, or vice versa. If you have an odd-numbered operation and an even-numbered
operation, you cannot accurately tell which one causally happened first.