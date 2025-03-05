### Direct messaging from producers to consumers 
A number of messaging systems use direct network communication between producers and consumers
without going via intermediary nodes: *  
UDP multicast is widely used in the financial industry for streams such as stock market feeds,
where low latency is important [[8](ch11.html#Lowenberger2009ac)]. Although UDP itself is
unreliable, application-level protocols can recover lost packets (the producer must remember
packets it has sent so that it can retransmit them on demand). *  
Brokerless messaging libraries such as ZeroMQ
[[9](ch11.html#Hintjens2013wf)] and nanomsg take a similar
approach, implementing publish/subscribe messaging over TCP or IP multicast. *  
StatsD [[10](ch11.html#Malpass2011wb)] and Brubeck
[[7](ch11.html#Marti2015ww)] use unreliable UDP messaging for
collecting metrics from all machines on the network and monitoring them. (In the StatsD protocol,
counter metrics are only correct if all messages are received; using UDP makes the metrics at best
approximate [[11](ch11.html#Plaetinck2016ta)]. See also
[“TCP Versus UDP”](ch08.html#sidebar_distributed_tcp_udp).) *   If the consumer exposes a service on the network, producers can make a direct
HTTP or RPC request (see [“Dataflow Through Services: REST and RPC”](ch04.html#sec_encoding_dataflow_rpc)) to push messages to the consumer. This is
the idea behind webhooks [[12](ch11.html#Lindsay2007tl)], a pattern in which a
callback URL of one service is registered with another service, and it makes a request to that URL
whenever an event occurs.