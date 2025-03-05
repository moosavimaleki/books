
A system is Byzantine fault-tolerant if it continues to operate correctly even if some of the
nodes are malfunctioning and not obeying the protocol, or if malicious attackers are interfering
with the network. This concern is relevant in certain specific circumstances. For example: *  
In aerospace environments, the data in a computer’s memory or CPU register could become corrupted
by radiation, leading it to respond to other nodes in arbitrarily unpredictable ways. Since a
system failure would be very expensive (e.g., an aircraft crashing and killing everyone on board,
or a rocket colliding with the International Space Station), flight control systems must tolerate
Byzantine faults [[81](ch08.html#Rushby2001vu), [82](ch08.html#Edge2013wn)]. *  
In a system with multiple participating organizations, some participants may attempt to cheat or
defraud others. In such circumstances, it is not safe for a node to simply trust another node’s
messages, since they may be sent with malicious intent. For example, peer-to-peer networks like
Bitcoin and other blockchains can be considered to be a way of getting mutually untrusting parties
to agree whether a transaction happened or not, without relying on a central authority
[[83](ch08.html#Miller2014wd)].