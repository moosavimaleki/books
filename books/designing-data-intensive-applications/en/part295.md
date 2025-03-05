A shared-memory architecture may offer limited fault tolerance—high-end machines have
hot-swappable components (you can replace disks, memory modules, and even CPUs without shutting down
the machines)—but it is definitely limited to a single geographic location. 
Another approach is the shared-disk architecture, which uses several machines with
independent CPUs and RAM, but stores data on an array of disks that is shared between the machines,
which are connected via a fast network.[ii](part02.html#idm140605776515616) This architecture is used
for some data warehousing workloads, but contention and the overhead of locking limit the
scalability of the shared-disk approach
[[2](part02.html#Stopford2009wv)]. ## Shared-Nothing Architectures 
By contrast, shared-nothing architectures
[[3](part02.html#Stonebraker1986tq)]
(sometimes called horizontal scaling or scaling out) have gained a lot of
popularity. In this approach, each machine or virtual machine running the database software is
called a node. Each node uses its CPUs, RAM, and disks independently. Any coordination
between nodes is done at the software level, using a conventional network.