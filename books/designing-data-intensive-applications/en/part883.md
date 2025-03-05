If the two join inputs are partitioned in the same way (using the same key, same hash function,
and same number of partitions), then the hash table approach can be used independently for each
partition. Distributed batch processing engines have a deliberately restricted programming model: callback
functions (such as mappers and reducers) are assumed to be stateless and to have no externally
visible side effects besides their designated output. This restriction allows the framework to hide
some of the hard distributed systems problems behind its abstraction: in the face of crashes and
network issues, tasks can be retried safely, and the output from any failed tasks is discarded. If
several tasks for a partition succeed, only one of them actually makes its output visible. Thanks to the framework, your code in a batch processing job does not need to worry about
implementing fault-tolerance mechanisms: the framework can guarantee that the final output of a job
is the same as if no faults had occurred, even though in reality various tasks perhaps had to be
retried. These reliable semantics are much stronger than what you usually have in online services
that handle user requests and that write to databases as a side effect of processing a request.