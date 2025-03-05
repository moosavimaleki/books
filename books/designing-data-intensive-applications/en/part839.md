*  MapReduce jobs often run many tasks in parallel. If all the mappers or reducers concurrently write
to the same output database, with a rate expected of a batch process, that database can easily be
overwhelmed, and its performance for queries is likely to suffer. This can in turn cause operational
problems in other parts of the system [[35](ch10.html#Kreps2014wm_ch10)]. *  Normally, MapReduce provides a clean all-or-nothing guarantee for job output: if a job succeeds,
the result is the output of running every task exactly once, even if some tasks failed and had to
be retried along the way; if the entire job fails, no output is produced. However, writing to an
external system from inside a job produces externally visible side effects that cannot be hidden
in this way. Thus, you have to worry about the results from partially completed jobs being visible
to other systems, and the complexities of Hadoop task attempts and speculative execution.