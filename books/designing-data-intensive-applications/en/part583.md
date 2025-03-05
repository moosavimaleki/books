*  
LWW cannot distinguish between writes that occurred sequentially in quick succession (in
[Figure 8-3](#fig_distributed_timestamps), client B’s increment definitely occurs after client A’s write)
and writes that were truly concurrent (neither writer was aware of the other). Additional
causality tracking mechanisms, such as version vectors, are needed in order to prevent violations
of causality (see [“Detecting Concurrent Writes”](ch05.html#sec_replication_concurrent)). *  It is possible for two nodes to independently generate writes with the same timestamp, especially
when the clock only has millisecond resolution. An additional tiebreaker value (which can simply
be a large random number) is required to resolve such conflicts, but this approach can also lead to
violations of causality [[53](ch08.html#Kingsbury2013ti_ch8)]. Thus, even though it is tempting to resolve conflicts by keeping the most “recent” value and
discarding others, it’s important to be aware that the definition of “recent” depends on a local
time-of-day clock, which may well be incorrect. Even with tightly NTP-synchronized clocks, you could
send a packet at timestamp 100 ms (according to the sender’s clock) and have it arrive at
timestamp 99 ms (according to the recipient’s clock)—so it appears as though the packet
arrived before it was sent, which is impossible.