
If you don’t care about fault tolerance, then satisfying the first three properties is easy: you can
just hardcode one node to be the “dictator,” and let that node make all of the decisions. However,
if that one node fails, then the system can no longer make any decisions. This is, in fact, what we
saw in the case of two-phase commit: if the coordinator fails, in-doubt participants cannot decide
whether to commit or abort. The termination property formalizes the idea of fault tolerance. It essentially says that a
consensus algorithm cannot simply sit around and do nothing forever—in other words, it must make
progress. Even if some nodes fail, the other nodes must still reach a decision. (Termination is a
liveness property, whereas the other three are safety properties—see
[“Safety and liveness”](ch08.html#sec_distributed_safety_liveness).) The system model of consensus assumes that when a node “crashes,” it suddenly disappears and never
comes back. (Instead of a software crash, imagine that there is an earthquake, and the datacenter
containing your node is destroyed by a landslide. You must assume that your node is buried under 30
feet of mud and is never going to come back online.) In this system model, any algorithm that has to
wait for a node to recover is not going to be able to satisfy the termination property. In
particular, 2PC does not meet the requirements for termination.