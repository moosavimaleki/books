Finally, we discussed techniques for achieving fault tolerance and exactly-once semantics in a
stream processor. As with batch processing, we need to discard the partial output of any failed
tasks. However, since a stream process is long-running and produces output continuously, we can’t
simply discard all output. Instead, a finer-grained recovery mechanism can be used, based on
microbatching, checkpointing, transactions, or idempotent writes. ##### Footnotes [i](ch11.html#idm140605757123312-marker) It’s possible to create a load balancing
scheme in which two consumers share the work of processing a partition by having both read the
full set of messages, but one of them only considers messages with even-numbered offsets while the other
deals with the odd-numbered offsets. Alternatively, you could spread message processing over a thread pool, but
that approach complicates consumer offset management. In general, single-threaded processing of a
partition is preferable, and parallelism can be increased by using more partitions. [ii](ch11.html#idm140605756499312-marker) Thank you to Kostas Kloudas from
the Flink community for coming up with this analogy.