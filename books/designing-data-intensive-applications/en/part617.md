Asynchronous model 
In this model, an algorithm is not allowed to make any timing assumptions—in fact, it does not
even have a clock (so it cannot use timeouts). Some algorithms can be designed for the
asynchronous model, but it is very restrictive. 
Moreover, besides timing issues, we have to consider node failures. The three most common system
models for nodes are: Crash-stop faults In the crash-stop model, an algorithm may assume that a node can fail in only one way, namely by
crashing. This means that the node may suddenly stop responding at any moment, and thereafter that
node is gone forever—it never comes back. Crash-recovery faults We assume that nodes may crash at any moment, and perhaps start responding again after some
unknown time. In the crash-recovery model, nodes are assumed to have stable storage (i.e.,
nonvolatile disk storage) that is preserved across crashes, while the in-memory state is assumed
to be lost.