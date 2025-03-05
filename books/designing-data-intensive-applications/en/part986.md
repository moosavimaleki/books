### Idempotence 
Our goal is to discard the partial output of any failed tasks so that they can be safely retried
without taking effect twice. Distributed transactions are one way of achieving that goal, but
another way is to rely on idempotence [[97](ch11.html#Helland2012id)]. An idempotent operation is one that you can perform multiple times, and it has the same effect as if
you performed it only once. For example, setting a key in a key-value store to some fixed value is
idempotent (writing the value again simply overwrites the value with an identical value), whereas
incrementing a counter is not idempotent (performing the increment again means the value is
incremented twice). 
Even if an operation is not naturally idempotent, it can often be made idempotent with a bit of
extra metadata. For example, when consuming messages from Kafka, every message has a persistent,
monotonically increasing offset. When writing a value to an external database, you can include the
offset of the message that triggered the last write with the value. Thus, you can tell whether an
update has already been applied, and avoid performing the same update again.