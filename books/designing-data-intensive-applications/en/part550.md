
Shared-nothing is not the only way of building systems, but it has become the dominant approach for
building internet services, for several reasons: it’s comparatively cheap because it
requires no special hardware, it can make use of commoditized cloud computing services, and it can
achieve high reliability through redundancy across multiple geographically distributed datacenters. 
The internet and most internal networks in datacenters (often Ethernet) are asynchronous packet
networks. In this kind of network, one node can send a message (a packet) to another node, but the
network gives no guarantees as to when it will arrive, or whether it will arrive at all. If you send
a request and expect a response, many things could go wrong (some of which are illustrated in
[Figure 8-1](#fig_distributed_network)): 1.  Your request may have been lost (perhaps someone unplugged a network cable). 2.  Your request may be waiting in a queue and will be delivered later (perhaps the network or the
recipient is overloaded).