
A variant approach, used in Apache Flink, is to periodically generate rolling checkpoints of state and
write them to durable storage
[[92](ch11.html#Tzoumas2015tt),
[93](ch11.html#Carbone2015wh)].
If a stream operator crashes, it can restart from its most recent checkpoint and discard any output
generated between the last checkpoint and the crash. The checkpoints are triggered by barriers in
the message stream, similar to the boundaries between microbatches, but without forcing a particular
window size. 
Within the confines of the stream processing framework, the microbatching and checkpointing
approaches provide the same exactly-once semantics as batch processing. However, as soon as output
leaves the stream processor (for example, by writing to a database, sending messages to an external
message broker, or sending emails), the framework is no longer able to discard the output of a
failed batch. In this case, restarting a failed task causes the external side effect to happen
twice, and microbatching or checkpointing alone is not sufficient to prevent this problem.