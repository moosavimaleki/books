
Subsequently, people found that MapReduce was too limiting and performed too badly for some types of
processing, so various other processing models were developed on top of Hadoop (we will see some of
them in [“Beyond MapReduce”](#sec_batch_beyond_mr)). Having two processing models, SQL and MapReduce, was not enough:
even more different models were needed! And due to the
openness of the Hadoop platform, it was feasible to implement a whole range of approaches, which
would not have been possible within the confines of a monolithic MPP database
[[58](ch10.html#Vavilapalli2013eu)]. 
Crucially, those various processing models can all be run on a single shared-use cluster of
machines, all accessing the same files on the distributed filesystem. In the Hadoop approach, there
is no need to import the data into several different specialized systems for different kinds of
processing: the system is flexible enough to support a diverse set of workloads within the same
cluster. Not having to move data around makes it a lot easier to derive value from the data, and a
lot easier to experiment with new processing models.