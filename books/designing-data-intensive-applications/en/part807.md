## MapReduce Job Execution 
MapReduce is a programming framework with which you can write code to process large datasets in a
distributed filesystem like HDFS. The easiest way of understanding it is by referring back to the
web server log analysis example in [“Simple Log Analysis”](#sec_batch_log_analysis). The pattern of data processing in
MapReduce is very similar to this example: 1.   Read a set of input files, and break it up into records. In the web server log
example, each record is one line in the log (that is, \n is the record separator). 2.  Call the mapper function to extract a key and value from each input record. In the preceding
example, the mapper function is awk '{print $7}': it extracts the URL ($7) as the key, and
leaves the value empty. 3.  Sort all of the key-value pairs by key. In the log example, this is done by the first sort
command.