Because the programming model deals with just one vertex at a time (sometimes called “thinking like a
vertex”), the framework may partition the graph in arbitrary ways. Ideally it would be partitioned
such that vertices are colocated on the same machine if they need to communicate a lot. However,
finding such an optimized partitioning is hard—in practice, the graph is often simply partitioned
by an arbitrarily assigned vertex ID, making no attempt to group related vertices together. As a result, graph algorithms often have a lot of cross-machine communication overhead, and the
intermediate state (messages sent between nodes) is often bigger than the original graph. The
overhead of sending messages over the network can significantly slow down distributed graph
algorithms. 
For this reason, if your graph can fit in memory on a single computer, it’s quite likely that a
single-machine (maybe even single-threaded) algorithm will outperform a distributed batch process
[[73](ch10.html#McSherry2015vx_ch10),
[74](ch10.html#Gog2015et)].
Even if the graph is bigger than memory, it can fit on the disks of a single computer,
single-machine processing using a framework such as GraphChi is a viable option
[[75](ch10.html#Kyrola2012uo)].
If the graph is too big to fit on a single machine, a distributed approach such as Pregel is
unavoidable; efficiently parallelizing graph algorithms is an area of ongoing research
[[76](ch10.html#Lenharth2016je)].