![ddia 0908](assets/ddia_0908.png) ###### Figure 9-8. Lamport timestamps provide a total ordering consistent with causality. A Lamport timestamp bears no relationship to a physical time-of-day clock, but it provides total
ordering: if you have two timestamps, the one with a greater counter value is the greater timestamp;
if the counter values are the same, the one with the greater node ID is the greater timestamp. So far this description is essentially the same as the even/odd counters described in the last
section. The key idea about Lamport timestamps, which makes them consistent with causality, is the
following: every node and every client keeps track of the maximum counter value it has seen so
far, and includes that maximum on every request. When a node receives a request or response with a
maximum counter value greater than its own counter value, it immediately increases its own counter
to that maximum. This is shown in [Figure 9-8](#fig_consistency_lamport_ts), where client A receives a counter value of 5 from
node 2, and then sends that maximum of 5 to node 1. At that time, node 1’s counter was only 1, but
it was immediately moved forward to 5, so the next operation had an incremented counter value of 6.