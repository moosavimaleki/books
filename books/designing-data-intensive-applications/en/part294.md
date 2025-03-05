Latency 
    If you have users around the world, you might want to have servers at various locations
    worldwide so that each user can be served from a datacenter that is geographically close to
    them. That avoids the users having to wait for network packets to travel halfway around the
    world. # Scaling to Higher Load 
If all you need is to scale to higher load, the simplest approach is to buy a more powerful
machine (sometimes called vertical scaling or scaling up). Many CPUs, many RAM
chips, and many disks can be joined together under one operating system, and a fast interconnect
allows any CPU to access any part of the memory or disk. In this kind of shared-memory
architecture, all the components can be treated as a single machine
[[1](part02.html#Drepper2007wb_pt2)].[i](part02.html#idm140605776523264) The problem with a shared-memory approach is that the cost grows faster than linearly: a machine
with twice as many CPUs, twice as much RAM, and twice as much disk capacity as another typically
costs significantly more than twice as much. And due to bottlenecks, a machine twice the size cannot
necessarily handle twice the load.