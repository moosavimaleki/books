*  
Timestamps from physical clocks are subject to clock skew, which can make them inconsistent with
causality. For example, see [Figure 8-3](ch08.html#fig_distributed_timestamps), which shows a scenario in which an
operation that happened causally later was actually assigned a lower
timestamp.[viii](ch09.html#idm140605759542720) *  In the case of the block allocator, one operation may be given a sequence number in the range from
1,001 to 2,000, and a causally later operation may be given a number in the range from 1 to 1,000.
Here, again, the sequence number is inconsistent with causality. ### Lamport timestamps 
Although the three sequence number generators just described are inconsistent with causality, there is
actually a simple method for generating sequence numbers that is consistent with causality. It is
called a Lamport timestamp, proposed in 1978 by Leslie Lamport
[[56](ch09.html#Lamport1978jq_ch9)],
in what is now one of the most-cited papers in the field of distributed systems. The use of Lamport timestamps is illustrated in [Figure 9-8](#fig_consistency_lamport_ts). Each node has a
unique identifier, and each node keeps a counter of the number of operations it has processed. The
Lamport timestamp is then simply a pair of (counter, node ID). Two nodes may sometimes have the
same counter value, but by including the node ID in the timestamp, each timestamp is made unique.