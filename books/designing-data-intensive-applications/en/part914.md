Databases and filesystems take the opposite approach: everything that is written to a database or
file is normally expected to be permanently recorded, at least until someone explicitly chooses to
delete it again. This difference in mindset has a big impact on how derived data is created. A key feature of batch
processes, as discussed in [Chapter 10](ch10.html#ch_batch), is that you can run them repeatedly, experimenting with the
processing steps, without risk of damaging the input (since the input is read-only). This is not the
case with AMQP/JMS-style messaging: receiving a message is destructive if the acknowledgment causes
it to be deleted from the broker, so you cannot run the same consumer again and expect to get the
same result. If you add a new consumer to a messaging system, it typically only starts receiving messages sent
after the time it was registered; any prior messages are already gone and cannot be recovered.
Contrast this with files and databases, where you can add a new client at any time, and it can read
data written arbitrarily far in the past (as long as it has not been explicitly overwritten or
deleted by the application).