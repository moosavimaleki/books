
There have been some attempts to build hybrid networks that support both circuit switching and
packet switching, such as ATM.[iii](ch08.html#idm140605760900048)
InfiniBand has some similarities
[[35](ch08.html#Mellanox2014ux)]: it implements end-to-end
flow control at the link layer, which reduces the need for queueing in the network, although it can
still suffer from delays due to link congestion
[[36](ch08.html#Santos2003ci)].
With careful use of quality of service (QoS, prioritization and scheduling of packets) and admission
control (rate-limiting senders), it is possible to emulate circuit switching on packet networks, or
provide statistically bounded delay [[25](ch08.html#Grosvenor2015vz),
[32](ch08.html#Keshav1997wb)]. ##### Latency and Resource Utilization 
More generally, you can think of variable delays as a consequence of dynamic resource partitioning. Say you have a wire between two telephone switches that can carry up to 10,000 simultaneous calls.
Each circuit that is switched over this wire occupies one of those call slots. Thus, you can think of
the wire as a resource that can be shared by up to 10,000 simultaneous users. The resource is
divided up in a static way: even if you’re the only call on the wire right now, and all other
9,999 slots are unused, your circuit is still allocated the same fixed amount of bandwidth as when
the wire is fully utilized.