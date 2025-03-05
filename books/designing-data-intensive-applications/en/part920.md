
This means that if a slow consumer cannot keep up with the rate of messages, and it falls so far
behind that its consumer offset points to a deleted segment, it will miss some of the messages.
Effectively, the log implements a bounded-size buffer that discards old messages when it gets full,
also known as a circular buffer or ring buffer. However, since that buffer is on disk, it can be
quite large. 
Let’s do a back-of-the-envelope calculation. At the time of writing, a typical large hard drive has
a capacity of 6 TB and a sequential write throughput of 150 MB/s. If you are writing
messages at the fastest possible rate, it takes about 11 hours to fill the drive. Thus, the disk can
buffer 11 hours’ worth of messages, after which it will start overwriting old messages. This ratio
remains the same, even if you use many hard drives and machines. In practice, deployments rarely use
the full write bandwidth of the disk, so the log can typically keep a buffer of several days’ or even
weeks’ worth of messages.