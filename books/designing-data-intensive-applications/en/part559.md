Imagine a fictitious system with a network that guaranteed a maximum delay for packets—every packet
is either delivered within some time d, or it is lost, but delivery never takes longer than d.
Furthermore, assume that you can guarantee that a non-failed node always handles a request within
some time r. In this case, you could guarantee that every successful request receives a response
within time 2d + r—and if you don’t receive a response within that time, you know
that either the network or the remote node is not working. If this was true,
2d + r would be a reasonable timeout to use. 
Unfortunately, most systems we work with have neither of those guarantees: asynchronous networks
have unbounded delays (that is, they try to deliver packets as quickly as possible, but there is
no upper limit on the time it may take for a packet to arrive), and most server implementations
cannot guarantee that they can handle requests within some maximum time (see
[“Response time guarantees”](#sec_distributed_clocks_realtime)). For failure detection, it’s not sufficient for the system to
be fast most of the time: if your timeout is low, it only takes a transient spike in round-trip
times to throw the system off-balance.