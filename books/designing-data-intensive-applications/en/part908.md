By centralizing the data in the broker, these systems can more easily tolerate clients that come and
go (connect, disconnect, and crash), and the question of durability is moved to the broker instead.
Some message brokers only keep messages in memory, while others (depending on configuration) write
them to disk so that they are not lost in case of a broker crash. Faced with slow consumers, they
generally allow unbounded queueing (as opposed to dropping messages or backpressure), although this choice
may also depend on the configuration. A consequence of queueing is also that consumers are generally asynchronous: when a producer sends
a message, it normally only waits for the broker to confirm that it has buffered the message and
does not wait for the message to be processed by consumers. The delivery to consumers will happen at
some undetermined future point in time—often within a fraction of a second, but sometimes
significantly later if there is a queue backlog.