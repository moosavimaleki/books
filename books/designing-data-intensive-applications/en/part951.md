On the other hand, deriving the current state from an event log also simplifies some aspects of
concurrency control. Much of the need for multi-object transactions (see
[“Single-Object and Multi-Object Operations”](ch07.html#sec_transactions_multi_object)) stems from a single user action requiring data to be changed in
several different places. With event sourcing, you can design an event such that it is a
self-contained description of a user action. The user action then requires only a single write in
one place—namely appending the events to the log—which is easy to make atomic. 
If the event log and the application state are partitioned in the same way (for example, processing
an event for a customer in partition 3 only requires updating partition 3 of the application state),
then a straightforward single-threaded log consumer needs no concurrency control for writes—by
construction, it only processes a single event at a time (see also [“Actual Serial Execution”](ch07.html#sec_transactions_serial)). The
log removes the nondeterminism of concurrency by defining a serial order of events in a partition
[[24](ch11.html#Kreps2013vs_ch11)]. If an event touches multiple state
partitions, a bit more work is required, which we will discuss in [Chapter 12](ch12.html#ch_future).