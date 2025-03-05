*  Mappers are often redundant: they just read back the same file that was just written by a reducer,
and prepare it for the next stage of partitioning and sorting. In many cases, the mapper code
could be part of the previous reducer: if the reducer output was partitioned and sorted in the
same way as mapper output, then reducers could be chained together directly, without interleaving
with mapper stages. *  Storing intermediate state in a distributed filesystem means those files are replicated across
several nodes, which is often overkill for such temporary data. ### Dataflow engines 
In order to fix these problems with MapReduce, several new execution engines for distributed batch
computations were developed, the most well known of which are Spark
[[61](ch10.html#Zaharia2012ve),
[62](ch10.html#Karau2015wf)],
Tez [[63](ch10.html#Saha2014vd),
[64](ch10.html#Saha2015dh)],
and Flink [[65](ch10.html#Tzoumas2015ws),
[66](ch10.html#Alexandrov2014jb)].
There are various differences in the way they are designed, but they have one thing in common: they
handle an entire workflow as one job, rather than breaking it up into independent subjobs.