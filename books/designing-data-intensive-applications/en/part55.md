
The architecture of systems that operate at large scale is usually highly specific to the
application—there is no such thing as a generic, one-size-fits-all scalable architecture
(informally known as magic scaling sauce). The problem may be the volume of reads, the volume of
writes, the volume of data to store, the complexity of the data, the response time requirements, the
access patterns, or (usually) some mixture of all of these plus many more issues. For example, a system that is designed to handle 100,000 requests per second, each 1 kB in
size, looks very different from a system that is designed for 3 requests per minute, each
2 GB in size—even though the two systems have the same data throughput. An architecture that scales well for a particular application is built around assumptions of which
operations will be common and which will be rare—the load parameters. If those assumptions turn
out to be wrong, the engineering effort for scaling is at best wasted, and at worst
counterproductive. In an early-stage startup or an unproven product it’s usually more important to
be able to iterate quickly on product features than it is to scale to some hypothetical future
load.