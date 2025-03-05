It would be unwise to assume that faults are rare and simply hope for the best. It is important to
consider a wide range of possible faults—even fairly unlikely ones—and to artificially create
such situations in your testing environment to see what happens. In distributed systems,
suspicion, pessimism, and paranoia pay off. ##### Building a Reliable System from Unreliable Components You may wonder whether this makes any sense—intuitively it may seem like a system can only be as
reliable as its least reliable component (its weakest link). This is not the case: in fact, it is
an old idea in computing to construct a more reliable system from a less reliable underlying base
[[11](ch08.html#vonNeumann1956vm)]. For example: *  
Error-correcting codes allow digital data to be transmitted accurately across a communication
channel that occasionally gets some bits wrong, for example due to radio interference on a
wireless network [[12](ch08.html#Hamming1997wd)]. *  
IP (the Internet Protocol) is unreliable: it may drop, delay, duplicate, or reorder packets.
TCP (the Transmission Control Protocol) provides a more reliable transport layer on top of IP: it
ensures that missing packets are retransmitted, duplicates are eliminated, and packets are
reassembled into the order in which they were sent.