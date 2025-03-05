Although these direct messaging systems work well in the situations for which they are designed,
they generally require the application code to be aware of the possibility of message loss. The
faults they can tolerate are quite limited: even if the protocols detect and retransmit packets that
are lost in the network, they generally assume that producers and consumers are constantly online. If a consumer is offline, it may miss messages that were sent while it is unreachable. Some
protocols allow the producer to retry failed message deliveries, but this approach may break down if
the producer crashes, losing the buffer of messages that it was supposed to retry. ### Message brokers 
A widely used alternative is to send messages via a message broker (also known as a message
queue), which is essentially a kind of database that is optimized for handling message streams
[[13](ch11.html#Gray1995tn)]. It runs as a server,
with producers and consumers connecting to it as clients. Producers write messages to the broker,
and consumers receive them by reading them from the broker.