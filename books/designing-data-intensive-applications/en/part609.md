## Byzantine Faults 
Fencing tokens can detect and block a node that is inadvertently acting in error (e.g., because it
hasn’t yet found out that its lease has expired). However, if the node deliberately wanted to
subvert the system’s guarantees, it could easily do so by sending messages with a fake fencing
token. In this book we assume that nodes are unreliable but honest: they may be slow or never respond (due
to a fault), and their state may be outdated (due to a GC pause or network delays), but we assume
that if a node does respond, it is telling the “truth”: to the best of its knowledge, it is
playing by the rules of the protocol. 
Distributed systems problems become much harder if there is a risk that nodes may “lie” (send
arbitrary faulty or corrupted responses)—for example, if a node may claim to have received a
particular message when in fact it didn’t. Such behavior is known as a Byzantine fault, and the
problem of reaching consensus in this untrusting environment is known as the Byzantine Generals Problem
[[77](ch08.html#Lamport1982fr)].