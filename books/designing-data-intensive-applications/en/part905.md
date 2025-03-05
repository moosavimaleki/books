2.  What happens if nodes crash or temporarily go offline—are any messages lost? As with databases,
durability may require some combination of writing to disk and/or replication (see the sidebar
[“Replication and Durability”](ch07.html#sidebar_transactions_durability)), which has a cost. If you can afford to sometimes lose
messages, you can probably get higher throughput and lower latency on the same hardware. Whether message loss is acceptable depends very much on the application. For example, with sensor
readings and metrics that are transmitted periodically, an occasional missing data point is perhaps
not important, since an updated value will be sent a short time later anyway. However, beware that
if a large number of messages are dropped, it may not be immediately apparent that the metrics are
incorrect [[7](ch11.html#Marti2015ww)]. If you are counting
events, it is more important that they are delivered reliably, since every lost message means
incorrect counters. 
A nice property of the batch processing systems we explored in [Chapter 10](ch10.html#ch_batch) is that they provide a
strong reliability guarantee: failed tasks are automatically retried, and partial output from failed
tasks is automatically discarded. This means the output is the same as if no failures had occurred,
which helps simplify the programming model. Later in this chapter we will examine how we can provide
similar guarantees in a streaming context.