*  A process may pause for a substantial amount of time at any point in its execution (perhaps due to
a stop-the-world garbage collector), be declared dead by other nodes, and then come back to life
again without realizing that it was paused. 
The fact that such partial failures can occur is the defining characteristic of distributed
systems. Whenever software tries to do anything involving other nodes, there is the possibility that
it may occasionally fail, or randomly go slow, or not respond at all (and eventually time out). In
distributed systems, we try to build tolerance of partial failures into software, so that the system
as a whole may continue functioning even when some of its constituent parts are broken. 
To tolerate faults, the first step is to detect them, but even that is hard. Most systems
don’t have an accurate mechanism of detecting whether a node has failed, so most distributed
algorithms rely on timeouts to determine whether a remote node is still available. However, timeouts
can’t distinguish between network and node failures, and variable network delay sometimes causes a
node to be falsely suspected of crashing. Moreover, sometimes a node can be in a degraded state: for
example, a Gigabit network interface could suddenly drop to 1 Kb/s throughput due to a driver
bug [[94](ch08.html#Do2013hc)].
Such a node that is “limping” but not dead can be even more difficult to deal with than a
cleanly failed node.