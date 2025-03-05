When you are writing software that runs on several computers, connected by a network, the situation
is fundamentally different. In distributed systems, we are no longer operating in an idealized
system model—we have no choice but to confront the messy reality of the physical world. And in
the physical world, a remarkably wide range of things can go wrong, as illustrated by this anecdote
[[4](ch08.html#Hale2010we)]: 
In my limited experience I’ve dealt with long-lived network partitions in a single data center (DC),
PDU [power distribution unit] failures, switch failures, accidental power cycles of whole racks,
whole-DC backbone failures, whole-DC power failures, and a hypoglycemic driver smashing his Ford
pickup truck into a DC’s HVAC [heating, ventilation, and air conditioning] system. And I’m not even
an ops guy. Coda Hale 
In a distributed system, there may well be some parts of the system that are broken in some
unpredictable way, even though other parts of the system are working fine. This is known as a
partial failure. The difficulty is that partial failures are nondeterministic: if you try to do
anything involving multiple nodes and the network, it may sometimes work and sometimes unpredictably
fail. As we shall see, you may not even know whether something succeeded or not, as the time it takes for a
message to travel across a network is also nondeterministic!