
There are many more interesting impossibility results in distributed systems
[[41](ch09.html#Lynch1989kj)],
and CAP has now been superseded by more precise results
[[2](ch09.html#Mahajan2011wz),
[42](ch09.html#Attiya2015dm)],
so it is of mostly historical interest today. ### Linearizability and network delays 
Although linearizability is a useful guarantee, surprisingly few systems are actually linearizable
in practice. For example, even RAM on a modern multi-core CPU is not linearizable
[[43](ch09.html#Sewell2010fj)]:
if a thread running on one CPU core writes to a memory address, and a thread on another CPU core
reads the same address shortly afterward, it is not guaranteed to read the value written by the
first thread (unless a memory barrier or fence
[[44](ch09.html#Thompson2011tr)]
is used). 
The reason for this behavior is that every CPU core has its own memory cache and store buffer.
Memory access first goes to the cache by default, and any changes are asynchronously written out to
main memory. Since accessing data in the cache is much faster than going to main memory
[[45](ch09.html#Drepper2007wb_ch9)], this feature is essential for
good performance on modern CPUs. However, there are now several copies of the data (one in main
memory, and perhaps several more in various caches), and these copies are asynchronously updated, so
linearizability is lost.