### Network congestion and queueing 
When driving a car, travel times on road networks often vary most due to traffic congestion.
Similarly, the variability of packet delays on computer networks is most often due to queueing
[[25](ch08.html#Grosvenor2015vz)]: *  If several different nodes simultaneously try to send packets to the same destination, the network
switch must queue them up and feed them into the destination network link one by one (as illustrated
in [Figure 8-2](#fig_distributed_switch_queueing)). On a busy network link, a packet may have to wait a while
until it can get a slot (this is called network congestion). If there is so much incoming data
that the switch queue fills up, the packet is dropped, so it needs to be resent—even though
the network is functioning fine. *  When a packet reaches the destination machine, if all CPU cores are currently busy, the incoming
request from the network is queued by the operating system until the application is ready to
handle it. Depending on the load on the machine, this may take an arbitrary length of time.