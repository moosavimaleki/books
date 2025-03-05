Tez is a fairly thin library that relies on the YARN shuffle service for the actual copying of data
between nodes [[58](ch10.html#Vavilapalli2013eu)], whereas Spark and
Flink are big frameworks that include their own network communication layer, scheduler, and
user-facing APIs. We will discuss those high-level APIs shortly. ### Fault tolerance 
An advantage of fully materializing intermediate state to a distributed filesystem is that it is
durable, which makes fault tolerance fairly easy in MapReduce: if a task fails, it can just be
restarted on another machine and read the same input again from the filesystem. 
Spark, Flink, and Tez avoid writing intermediate state to HDFS, so they take a different approach to
tolerating faults: if a machine fails and the intermediate state on that machine is lost, it is
recomputed from other data that is still available (a prior intermediary stage if possible, or
otherwise the original input data, which is normally on HDFS).