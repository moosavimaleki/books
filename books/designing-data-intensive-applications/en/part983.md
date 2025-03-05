The same issue of fault tolerance arises in stream processing, but it is less straightforward to
handle: waiting until a task is finished before making its output visible is not an option, because
a stream is infinite and so you can never finish processing it. ### Microbatching and checkpointing 
One solution is to break the stream into small blocks, and treat each block like a miniature batch
process. This approach is called microbatching, and it is used in Spark Streaming
[[91](ch11.html#Zaharia2012wa)]. The
batch size is typically around one second, which is the result of a performance compromise: smaller
batches incur greater scheduling and coordination overhead, while larger batches mean a longer delay
before results of the stream processor become visible. 
Microbatching also implicitly provides a tumbling window equal to the batch size (windowed by
processing time, not event timestamps); any jobs that require larger windows need to explicitly
carry over state from one microbatch to the next.