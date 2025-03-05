## Sequence Number Ordering 
Although causality is an important theoretical concept, actually keeping track of all causal
dependencies can become impractical. In many applications, clients read lots of data before writing
something, and then it is not clear whether the write is causally dependent on all or only some of
those prior reads. Explicitly tracking all the data that has been read would mean a large overhead. 
However, there is a better way: we can use sequence numbers or timestamps to order events. A
timestamp need not come from a time-of-day clock (or physical clock, which have many problems, as
discussed in [“Unreliable Clocks”](ch08.html#sec_distributed_clocks)). It can instead come from a logical clock, which
is an algorithm to generate a sequence of numbers to identify operations, typically using counters
that are incremented for every operation. 
Such sequence numbers or timestamps are compact (only a few bytes in size), and they provide a
total order: that is, every operation has a unique sequence number, and you can always compare two
sequence numbers to determine which is greater (i.e., which operation happened later).