### Sort-merge joins 
Recall that the purpose of the mapper is to extract a key and value from each input record. In the
case of [Figure 10-2](#fig_batch_join_example), this key would be the user ID: one set of mappers would go over
the activity events (extracting the user ID as the key and the activity event as the value), while
another set of mappers would go over the user database (extracting the user ID as the key and the
user’s date of birth as the value). This process is illustrated in [Figure 10-3](#fig_batch_join_reduce). ![ddia 1003](assets/ddia_1003.png) ###### Figure 10-3. A reduce-side sort-merge join on user ID. If the input datasets are partitioned into multiple files, each could be processed with multiple mappers in parallel. 
When the MapReduce framework partitions the mapper output by key and then sorts the key-value
pairs, the effect is that all the activity events and the user record with the same user ID become
adjacent to each other in the reducer input. The MapReduce job can even arrange the records to be
sorted such that the reducer always sees the record from the user database first, followed by the
activity events in timestamp order—this technique is known as a secondary sort
[[26](ch10.html#White2015vl)].