Although a single-leader database can provide linearizability without executing a consensus
algorithm on every write, it still requires consensus to maintain its leadership and for leadership
changes. Thus, in some sense, having a leader only “kicks the can down the road”: consensus is still
required, only in a different place, and less frequently. The good news is that fault-tolerant
algorithms and systems for consensus exist, and we briefly discussed them in this chapter. Tools like ZooKeeper play an important role in providing an “outsourced” consensus, failure
detection, and membership service that applications can use. It’s not easy to use, but it is much
better than trying to develop your own algorithms that can withstand all the problems discussed in
[Chapter 8](ch08.html#ch_distributed). If you find yourself wanting to do one of those things that is reducible to
consensus, and you want it to be fault-tolerant, then it is advisable to use something like
ZooKeeper.