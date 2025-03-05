Later, in [Part III](part03.html#part_systems) of this book, we will discuss how you can
take several (potentially distributed) datastores and integrate them into a larger system,
satisfying the needs of a complex application. But first, let’s talk about distributed
data. ##### Footnotes [i](part02.html#idm140605776523264-marker) In
a large machine, although any CPU can access any part of memory, some banks of memory are closer to
one CPU than to others (this is called nonuniform memory access, or NUMA
[[1](part02.html#Drepper2007wb_pt2)]). To make efficient use of this
architecture, the processing needs to be broken down so that each CPU mostly accesses memory that is
nearby—which means that partitioning is still required, even when ostensibly running on one
machine. [ii](part02.html#idm140605776515616-marker) Network
Attached Storage (NAS) or Storage Area Network (SAN). ##### References [[1](part02.html#Drepper2007wb_pt2-marker)] Ulrich Drepper:
“[What Every Programmer Should Know About Memory](http://www.akkadia.org/drepper/cpumemory.pdf),”
akkadia.org, November 21, 2007. [[2](part02.html#Stopford2009wv-marker)] Ben Stopford:
“[Shared
Nothing vs. Shared Disk Architectures: An Independent View](http://www.benstopford.com/2009/11/24/understanding-the-shared-nothing-architecture/),” benstopford.com, November 24,
2009.