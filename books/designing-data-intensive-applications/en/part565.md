
When you make a call over the telephone network, it establishes a circuit: a fixed, guaranteed
amount of bandwidth is allocated for the call, along the entire route between the two callers. This
circuit remains in place until the call ends
[[32](ch08.html#Keshav1997wb)].
For example, an ISDN network runs at a fixed rate of 4,000 frames per second. When a call is
established, it is allocated 16 bits of space within each frame (in each direction). Thus, for the
duration of the call, each side is guaranteed to be able to send exactly 16 bits of audio data every
250 microseconds
[[33](ch08.html#CiscoISDN),
[34](ch08.html#Kyas1995ug)]. 
This kind of network is synchronous: even as data passes through several routers, it does not
suffer from queueing, because the 16 bits of space for the call have already been reserved in the
next hop of the network. And because there is no queueing, the maximum end-to-end latency of the
network is fixed. We call this a bounded delay.