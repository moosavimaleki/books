However, there are also problems with the MapReduce execution model itself, which are not fixed by
adding another level of abstraction and which manifest themselves as poor performance for some
kinds of processing. On the one hand, MapReduce is very robust: you can use it to process almost
arbitrarily large quantities of data on an unreliable multi-tenant system with frequent task
terminations, and it will still get the job done (albeit slowly). On the other hand, other tools are
sometimes orders of magnitude faster for some kinds of processing. In the rest of this chapter, we will look at some of those alternatives for batch processing. In
[Chapter 11](ch11.html#ch_stream) we will move to stream processing, which can be regarded as another way of speeding up
batch processing. ## Materialization of Intermediate State 
As discussed previously, every MapReduce job is independent from every other job. The main contact
points of a job with the rest of the world are its input and output directories on the distributed
filesystem. If you want the output of one job to become the input to a second job, you need to
configure the second job’s input directory to be the same as the first job’s output directory, and
an external workflow scheduler must start the second job only once the first job has completed.