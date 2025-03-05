## Fault Tolerance 
In the final section of this chapter, let’s consider how stream processors can tolerate faults. We
saw in [Chapter 10](ch10.html#ch_batch) that batch processing frameworks can tolerate faults fairly easily: if a task in
a MapReduce job fails, it can simply be started again on another machine, and the output of the
failed task is discarded. This transparent retry is possible because input files are immutable, each
task writes its output to a separate file on HDFS, and output is only made visible when a task
completes successfully. 
In particular, the batch approach to fault tolerance ensures that the output of the batch job is the
same as if nothing had gone wrong, even if in fact some tasks did fail. It appears as though every
input record was processed exactly once—no records are skipped, and none are processed twice.
Although restarting tasks means that records may in fact be processed multiple times, the visible
effect in the output is as if they had only been processed once. This principle is known as
exactly-once semantics, although effectively-once would be a more descriptive term
[[90](ch11.html#Klang2016mw)].