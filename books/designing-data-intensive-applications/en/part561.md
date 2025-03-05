*  
In virtualized environments, a running operating system is often paused for tens of milliseconds
while another virtual machine uses a CPU core. During this time, the VM cannot consume any data
from the network, so the incoming data is queued (buffered) by the virtual machine monitor
[[26](ch08.html#Wang2010ja)],
further increasing the variability of network delays. *  
TCP performs flow control (also known as congestion avoidance or backpressure), in which a
node limits its own rate of sending in order to avoid overloading a network link or the receiving
node [[27](ch08.html#Jacobson1988gl)].
This means additional queueing at the sender before the data even enters the network. ![ddia 0802](assets/ddia_0802.png) ###### Figure 8-2. If several machines send network traffic to the same destination, its switch queue can fill up. Here, ports 1, 2, and 4 are all trying to send packets to port 3. Moreover, TCP considers a packet to be lost if it is not acknowledged within some timeout (which is
calculated from observed round-trip times), and lost packets are automatically retransmitted.
Although the application does not see the packet loss and retransmission, it does see the resulting
delay (waiting for the timeout to expire, and then waiting for the retransmitted packet to be
acknowledged).