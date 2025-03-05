A long timeout means a long wait until a node is declared dead (and during this time, users may have
to wait or see error messages). A short timeout detects faults faster, but carries a higher risk of
incorrectly declaring a node dead when in fact it has only suffered a temporary slowdown (e.g., due
to a load spike on the node or the network). Prematurely declaring a node dead is problematic: if the node is actually alive and in the middle of
performing some action (for example, sending an email), and another node takes over, the action may
end up being performed twice. We will discuss this issue in more detail in
[“Knowledge, Truth, and Lies”](#sec_distributed_truth), and in
Chapters [9](ch09.html#ch_consistency)
and [11](ch11.html#ch_stream). 
When a node is declared dead, its responsibilities need to be transferred to other nodes, which
places additional load on other nodes and the network. If the system is already struggling with high
load, declaring nodes dead prematurely can make the problem worse. In particular, it could happen
that the node actually wasn’t dead but only slow to respond due to overload; transferring its load
to other nodes can cause a cascading failure (in the extreme case, all nodes declare each other
dead, and everything stops working).