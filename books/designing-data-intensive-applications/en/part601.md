## The Truth Is Defined by the Majority 
Imagine a network with an asymmetric fault: a node is able to receive all messages sent to it, but
any outgoing messages from that node are dropped or delayed
[[19](ch08.html#Donges2012tt)]. Even though that node is working
perfectly well, and is receiving requests from other nodes, the other nodes cannot hear its
responses. After some timeout, the other nodes declare it dead, because they haven’t heard from the
node. The situation unfolds like a nightmare: the semi-disconnected node is dragged to the
graveyard, kicking and screaming “I’m not dead!”—but since nobody can hear its screaming, the
funeral procession continues with stoic determination. In a slightly less nightmarish scenario, the semi-disconnected node may notice that the messages it
is sending are not being acknowledged by other nodes, and so realize that there must be a fault
in the network. Nevertheless, the node is wrongly declared dead by the other nodes, and the
semi-disconnected node cannot do anything about it.