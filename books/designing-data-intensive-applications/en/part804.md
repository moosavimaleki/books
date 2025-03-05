However, the biggest limitation of Unix tools is that they run only on a single machine—and
that’s where tools like Hadoop come in. # MapReduce and Distributed Filesystems 
MapReduce is a bit like Unix tools, but distributed across potentially thousands of machines. Like
Unix tools, it is a fairly blunt, brute-force, but surprisingly effective tool. A single MapReduce
job is comparable to a single Unix process: it takes one or more inputs and produces one or more
outputs. As with most Unix tools, running a MapReduce job normally does not modify the input and does not
have any side effects other than producing the output. The output files are written once, in a
sequential fashion (not modifying any existing part of a file once it has been written). 
While Unix tools use stdin and stdout as input and output, MapReduce jobs read and write files
on a distributed filesystem. In Hadoop’s implementation of MapReduce, that filesystem is called HDFS
(Hadoop Distributed File System), an open source reimplementation of the Google File System (GFS)
[[19](ch10.html#Ghemawat2003dy)].