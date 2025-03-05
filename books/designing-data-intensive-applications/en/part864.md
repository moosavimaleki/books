
To enable this recomputation, the framework must keep track of how a given piece of data was
computed—which input partitions it used, and which operators were applied to it. Spark uses the
resilient distributed dataset (RDD) abstraction for tracking the ancestry of data
[[61](ch10.html#Zaharia2012ve)], while Flink checkpoints operator state,
allowing it to resume running an operator that ran into a fault during its execution
[[66](ch10.html#Alexandrov2014jb)]. 
When recomputing data, it is important to know whether the computation is deterministic: that is,
given the same input data, do the operators always produce the same output? This question matters if some of
the lost data has already been sent to downstream operators. If the operator is restarted and the
recomputed data is not the same as the original lost data, it becomes very hard for downstream
operators to resolve the contradictions between the old and new data. The solution in the case of
nondeterministic operators is normally to kill the downstream operators as well, and run them again
on the new data.