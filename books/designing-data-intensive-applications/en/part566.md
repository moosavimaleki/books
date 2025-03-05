### Can we not simply make network delays predictable? 
Note that a circuit in a telephone network is very different from a TCP connection: a circuit is a
fixed amount of reserved bandwidth which nobody else can use while the circuit is established,
whereas the packets of a TCP connection opportunistically use whatever network bandwidth is
available. You can give TCP a variable-sized block of data (e.g., an email or a web page), and it
will try to transfer it in the shortest time possible. While a TCP connection is idle, it doesn’t
use any bandwidth.[ii](ch08.html#idm140605760908512) 
If datacenter networks and the internet were circuit-switched networks, it would be possible to
establish a guaranteed maximum round-trip time when a circuit was set up. However, they are not:
Ethernet and IP are packet-switched protocols, which suffer from queueing and thus unbounded delays
in the network. These protocols do not have the concept of a circuit.