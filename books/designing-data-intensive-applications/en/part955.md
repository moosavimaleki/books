3.  You can process one or more input streams to produce one or more output streams. Streams may go
through a pipeline consisting of several such processing stages before they eventually end up at
an output (option 1 or 2). 
In the rest of this chapter, we will discuss option 3: processing streams to produce other, derived
streams. A piece of code that processes streams like this is known as an operator or a job. It
is closely related to the Unix processes and MapReduce jobs we discussed in [Chapter 10](ch10.html#ch_batch), and
the pattern of dataflow is similar: a stream processor consumes input streams in a read-only
fashion and writes its output to a different location in an append-only fashion. 
The patterns for partitioning and parallelization in stream processors are also very similar to
those in MapReduce and the dataflow engines we saw in [Chapter 10](ch10.html#ch_batch), so we won’t repeat those topics
here. Basic mapping operations such as transforming and filtering records also work the same.