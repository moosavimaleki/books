1.  Wait for the leader to recover, and accept that the system will be blocked in the meantime. Many
XA/JTA transaction coordinators choose this option. This approach does not fully solve consensus
because it does not satisfy the termination property: if the leader does not recover, the system
can be blocked forever. 2.  Manually fail over by getting humans to choose a new leader node and reconfigure the system to use
it. Many relational databases take this approach. It is a kind of consensus by “act of God”—the
human operator, outside of the computer system, makes the decision. The speed of failover is
limited by the speed at which humans can act, which is generally slower than computers. 3.  Use an algorithm to automatically choose a new leader. This approach requires a consensus
algorithm, and it is advisable to use a proven algorithm that correctly handles adverse network
conditions [[107](ch09.html#Kingsbury2015uk)].