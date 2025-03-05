
When the input is a file (a sequence of bytes), the first processing step is usually to parse it
into a sequence of records. In a stream processing context, a record is more commonly known as an
event, but it is essentially the same thing: a small, self-contained, immutable object containing
the details of something that happened at some point in time. An event usually contains a timestamp
indicating when it happened according to a time-of-day clock (see [“Monotonic Versus Time-of-Day Clocks”](ch08.html#sec_distributed_monotonic_timeofday)). For example, the thing that happened might be an action that a user took, such as viewing a page or
making a purchase. It might also originate from a machine, such as a periodic measurement from a
temperature sensor, or a CPU utilization metric. In the example of [“Batch Processing with Unix Tools”](ch10.html#sec_batch_unix), each line of
the web server log is an event. An event may be encoded as a text string, or JSON, or perhaps in some binary form, as discussed in
[Chapter 4](ch04.html#ch_encoding). This encoding allows you to store an event, for example by appending it to a file,
inserting it into a relational table, or writing it to a document database. It also allows you to
send the event over the network to another node in order to process it.