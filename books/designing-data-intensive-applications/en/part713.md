In these cases, it is not sufficient to simply send a commit request to all of the nodes and
independently commit the transaction on each one. In doing so, it could easily happen that the
commit succeeds on some nodes and fails on other nodes, which would violate the atomicity guarantee: *  
Some nodes may detect a constraint violation or conflict, making an abort necessary, while other
nodes are successfully able to commit. *  Some of the commit requests might be lost in the network, eventually aborting due to a timeout,
while other commit requests get through. *  Some nodes may crash before the commit record is fully written and roll back on recovery, while
others successfully commit. If some nodes commit the transaction but others abort it, the nodes become inconsistent with each
other (like in [Figure 7-3](ch07.html#fig_transactions_atomicity)). And once a transaction has been committed on one
node, it cannot be retracted again if it later turns out that it was aborted on another node. For
this reason, a node must only commit once it is certain that all other nodes in the transaction are
also going to commit.