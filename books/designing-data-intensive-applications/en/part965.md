A batch process may read a year’s worth of historical events within a few minutes; in most cases, the
timeline of interest is the year of history, not the few minutes of processing. Moreover, using the
timestamps in the events allows the processing to be deterministic: running the same process again on
the same input yields the same result (see [“Fault tolerance”](ch10.html#sec_batch_materialize_ft)). 
On the other hand, many stream processing frameworks use the local system clock on the processing
machine (the processing time) to determine windowing
[[79](ch11.html#Akidau2016tb)].
This approach has the advantage of being simple, and it is reasonable if the delay between event
creation and event processing is negligibly short. However, it breaks down if there is any
significant processing lag—i.e., if the processing may happen noticeably later than the time at
which the event actually occurred. ### Event time versus processing time 
There are many reasons why processing may be delayed: queueing, network faults (see
[“Unreliable Networks”](ch08.html#sec_distributed_networks)), a performance issue leading to contention in the message broker or
processor, a restart of the stream consumer, or reprocessing of past events (see
[“Replaying old messages”](#sec_stream_replay)) while recovering from a fault or after fixing a bug in the code.