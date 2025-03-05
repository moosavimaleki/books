
The two main problems that distributed batch processing frameworks need to solve are: Partitioning In MapReduce, mappers are partitioned according to input file blocks. The output of mappers is
repartitioned, sorted, and merged into a configurable number of reducer partitions. The purpose of
this process is to bring all the related data—e.g., all the records with the same key—together in
the same place. 
Post-MapReduce dataflow engines try to avoid sorting unless it is required, but they otherwise take
a broadly similar approach to partitioning. Fault tolerance MapReduce frequently writes to disk, which makes it easy to recover from an individual
failed task without restarting the entire job but slows down execution in the failure-free
case. Dataflow engines perform less materialization of intermediate state and keep more in memory,
which means that they need to recompute more data if a node fails. Deterministic operators reduce
the amount of data that needs to be recomputed.