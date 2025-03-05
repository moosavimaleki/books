Most of these algorithms actually don’t directly use the formal model described here (proposing and
deciding on a single value, while satisfying the agreement, integrity, validity, and termination
properties). Instead, they decide on a sequence of values, which makes them total order
broadcast algorithms, as discussed previously in this chapter (see
[“Total Order Broadcast”](#sec_consistency_total_order)). Remember that total order broadcast requires messages to be delivered exactly once, in the same
order, to all nodes. If you think about it, this is equivalent to performing several rounds of
consensus: in each round, nodes propose the message that they want to send next, and then decide on
the next message to be delivered in the total order
[[67](ch09.html#Chandra1996cp)]. 
So, total order broadcast is equivalent to repeated rounds of consensus (each consensus decision
corresponding to one message delivery): *  Due to the agreement property of consensus, all nodes decide to deliver the same messages in the
same order.