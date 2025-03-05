### MapReduce workflows 
The range of problems you can solve with a single MapReduce job is limited. Referring back to the
log analysis example, a single MapReduce job could determine the number of page views per URL, but
not the most popular URLs, since that requires a second round of sorting. 
Thus, it is very common for MapReduce jobs to be chained together into workflows, such that the
output of one job becomes the input to the next job. The Hadoop MapReduce framework does not have
any particular support for workflows, so this chaining is done implicitly by directory name: the
first job must be configured to write its output to a designated directory in HDFS, and the second
job must be configured to read that same directory name as its input. From the MapReduce framework’s
point of view, they are two independent jobs. Chained MapReduce jobs are therefore less like pipelines of Unix commands (which pass the output of
one process as input to another process directly, using only a small in-memory buffer) and more
like a sequence of commands where each command’s output is written to a temporary file, and the next
command reads from the temporary file. This design has advantages and disadvantages, which we will
discuss in [“Materialization of Intermediate State”](#sec_batch_materialize).