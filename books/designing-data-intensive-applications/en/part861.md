*  For broadcast hash joins, the same output from one operator can be sent to all partitions of
the join operator. 
This style of processing engine is based on research systems like Dryad
[[67](ch10.html#Isard2007fe)]
and Nephele [[68](ch10.html#Warneke2009en)], and it
offers several advantages compared to the MapReduce model: *  Expensive work such as sorting need only be performed in places where it is actually required,
rather than always happening by default between every map and reduce stage. *  There are no unnecessary map tasks, since the work done by a mapper can often be
incorporated into the preceding reduce operator (because a mapper does not change the partitioning
of a dataset). *  
Because all joins and data dependencies in a workflow are explicitly declared, the scheduler has
an overview of what data is required where, so it can make locality optimizations. For example, it
can try to place the task that consumes some data on the same machine as the task that produces
it, so that the data can be exchanged through a shared memory buffer rather than having to copy
it over the network.