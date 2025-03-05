
Since they explicitly model the flow of data through several processing stages, these systems are
known as dataflow engines. Like MapReduce, they work by repeatedly calling a user-defined function
to process one record at a time on a single thread. They parallelize work by partitioning inputs,
and they copy the output of one function over the network to become the input to another function. 
Unlike in MapReduce, these functions need not take the strict roles of alternating map and reduce,
but instead can be assembled in more flexible ways. We call these functions operators, and the
dataflow engine provides several different options for connecting one operator’s output to another’s
input: *  One option is to repartition and sort records by key, like in the shuffle stage of MapReduce
(see [“Distributed execution of MapReduce”](#sec_batch_mapreduce_dist)). This feature enables sort-merge joins and grouping in the same
way as in MapReduce. *  Another possibility is to take several inputs and to partition them in the same way, but skip
the sorting. This saves effort on partitioned hash joins, where the partitioning of records is
important but the order is irrelevant because building the hash table randomizes the order
anyway.