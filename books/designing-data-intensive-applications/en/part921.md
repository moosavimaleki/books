Regardless of how long you retain messages, the throughput of a log remains more or less constant,
since every message is written to disk anyway [[18](ch11.html#Kreps2011wl)].
This behavior is in contrast to messaging systems that keep messages in memory by default and only
write them to disk if the queue grows too large: such systems are fast when queues are short and
become much slower when they start writing to disk, so the throughput depends on the amount of
history retained. ### When consumers cannot keep up with producers 
At the beginning of [“Messaging Systems”](#sec_stream_messaging) we discussed three choices of what to do if a consumer
cannot keep up with the rate at which producers are sending messages: dropping messages, buffering,
or applying backpressure. In this taxonomy, the log-based approach is a form of buffering with a
large but fixed-size buffer (limited by the available disk space). If a consumer falls so far behind that the messages it requires are older than what is retained on
disk, it will not be able to read those messages—so the broker effectively drops old messages that
go back further than the size of the buffer can accommodate. You can monitor how far a consumer is
behind the head of the log, and raise an alert if it falls behind significantly. As the buffer is
large, there is enough time for a human operator to fix the slow consumer and allow it to catch up
before it starts missing messages.