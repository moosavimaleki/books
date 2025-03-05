
If the connection to a client is closed or times out without the broker receiving an acknowledgment,
it assumes that the message was not processed, and therefore it delivers the message again to
another consumer. (Note that it could happen that the message actually was fully processed, but
the acknowledgment was lost in the network. Handling this case requires an atomic commit protocol,
as discussed in [“Distributed Transactions in Practice”](ch09.html#sec_consistency_dist_trans).) When combined with load balancing, this redelivery behavior has an interesting effect on the
ordering of messages. In [Figure 11-2](#fig_stream_redelivery), the consumers generally process messages in the
order they were sent by producers. However, consumer 2 crashes while processing message m3, at the
same time as consumer 1 is processing message m4. The unacknowledged message m3 is subsequently
redelivered to consumer 1, with the result that consumer 1 processes messages in the order m4, m3,
m5. Thus, m3 and m4 are not delivered in the same order as they were sent by producer 1.