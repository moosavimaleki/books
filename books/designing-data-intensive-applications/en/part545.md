
In this book we focus on systems for implementing internet services, which usually look very
different from supercomputers: *  Many internet-related applications are online, in the sense that they need to be able to serve
users with low latency at any time. Making the service unavailable—for example, stopping the
cluster for repair—is not acceptable. In contrast, offline (batch) jobs like weather
simulations can be stopped and restarted with fairly low impact. *  
Supercomputers are typically built from specialized hardware, where each node is quite reliable,
and nodes communicate through shared memory and remote direct memory access (RDMA). On the other
hand, nodes in cloud services are built from commodity machines, which can provide equivalent
performance at lower cost due to economies of scale, but also have higher failure rates. *  
Large datacenter networks are often based on IP and Ethernet, arranged in Clos topologies to
provide high bisection bandwidth
[[9](ch08.html#Singh2015fc)].
Supercomputers often use specialized network topologies, such as multi-dimensional meshes and toruses
[[10](ch08.html#Lockwood2014uz)],
which yield better performance for HPC workloads with known communication patterns.