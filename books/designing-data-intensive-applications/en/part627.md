However, as discussed in the introduction to [Part II](part02.html#part_distributed_data), scalability is not the only
reason for wanting to use a distributed system. Fault tolerance and low latency (by placing data
geographically close to users) are equally important goals, and those things cannot be achieved with
a single node. In this chapter we also went on some tangents to explore whether the unreliability of networks,
clocks, and processes is an inevitable law of nature. We saw that it isn’t: it is possible to give
hard real-time response guarantees and bounded delays in networks, but doing so is very expensive and
results in lower utilization of hardware resources. Most non-safety-critical systems choose cheap
and unreliable over expensive and reliable. We also touched on supercomputers, which assume reliable components and thus have to be stopped and
restarted entirely when a component does fail. By contrast, distributed systems can run forever
without being interrupted at the service level, because all faults and maintenance can be handled at
the node level—at least in theory. (In practice, if a bad configuration change is rolled out to
all nodes, that will still bring a distributed system to its knees.)