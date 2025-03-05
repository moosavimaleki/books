The process of writing out this intermediate state to files is called materialization. (We came
across the term previously in the context of materialized views, in
[“Aggregation: Data Cubes and Materialized Views”](ch03.html#sec_storage_materialized_views). It means to eagerly compute the result of some operation and
write it out, rather than computing it on demand when requested.) By contrast, the log analysis example at the beginning of the chapter used Unix pipes to connect the
output of one command with the input of another. Pipes do not fully materialize the intermediate
state, but instead stream the output to the input incrementally, using only a small in-memory
buffer. MapReduce’s approach of fully materializing intermediate state has downsides compared to Unix pipes: *  A MapReduce job can only start when all tasks in the preceding jobs (that generate its inputs)
have completed, whereas processes connected by a Unix pipe are started at the same time, with
output being consumed as soon as it is produced. Skew or varying load on different machines means
that a job often has a few straggler tasks that take much longer to complete than the others.
Having to wait until all of the preceding job’s tasks have completed slows down the execution of
the workflow as a whole.