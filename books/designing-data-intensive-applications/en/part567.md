
Why do datacenter networks and the internet use packet switching? The answer is that they are
optimized for bursty traffic. A circuit is good for an audio or video call, which needs to
transfer a fairly constant number of bits per second for the duration of the call. On the other
hand, requesting a web page, sending an email, or transferring a file doesn’t have any particular
bandwidth requirement—we just want it to complete as quickly as possible. If you wanted to transfer a file over a circuit, you would have to guess a bandwidth allocation. If
you guess too low, the transfer is unnecessarily slow, leaving network capacity unused. If you guess
too high, the circuit cannot be set up (because the network cannot allow a circuit to be created if
its bandwidth allocation cannot be guaranteed). Thus, using circuits for bursty data transfers
wastes network capacity and makes transfers unnecessarily slow. By contrast, TCP dynamically adapts
the rate of data transfer to the available network capacity.