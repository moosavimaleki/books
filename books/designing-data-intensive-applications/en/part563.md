All of these factors contribute to the variability of network delays. Queueing delays have an
especially wide range when a system is close to its maximum capacity: a system with plenty of spare
capacity can easily drain queues, whereas in a highly utilized system, long queues can build up very
quickly. 
In public clouds and multi-tenant datacenters, resources are shared among many customers: the
network links and switches, and even each machine’s network interface and CPUs (when running on
virtual machines), are shared. Batch workloads such as MapReduce (see [Chapter 10](ch10.html#ch_batch)) can easily
saturate network links. As you have no control over or insight into other customers’ usage of the shared
resources, network delays can be highly variable if someone near you (a noisy neighbor) is
using a lot of resources [[28](ch08.html#Philips2014tr),
[29](ch08.html#Newman2012vf)]. 
In such environments, you can only choose timeouts experimentally: measure the distribution of
network round-trip times over an extended period, and over many machines, to determine the expected
variability of delays. Then, taking into account your application’s characteristics, you can
determine an appropriate trade-off between failure detection delay and risk of premature timeouts.