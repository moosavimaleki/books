*  It is usually sufficient for intermediate state between operators to be kept in memory or written
to local disk, which requires less I/O than writing it to HDFS (where it must be replicated to
several machines and written to disk on each replica). MapReduce already uses this optimization
for mapper output, but dataflow engines generalize the idea to all intermediate state. *  Operators can start executing as soon as their input is ready; there is no need to wait for the
entire preceding stage to finish before the next one starts. *  
Existing Java Virtual Machine (JVM) processes can be reused to run new operators, reducing startup
overheads compared to MapReduce (which launches a new JVM for each task). You can use dataflow engines to implement the same computations as MapReduce workflows, and they
usually execute significantly faster due to the optimizations described here. Since operators are a
generalization of map and reduce, the same processing code can run on either execution engine:
workflows implemented in Pig, Hive, or Cascading can be switched from MapReduce to Tez or Spark with
a simple configuration change, without modifying code
[[64](ch10.html#Saha2015dh)].