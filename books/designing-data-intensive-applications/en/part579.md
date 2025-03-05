
Such accuracy can be achieved using GPS receivers, the Precision Time Protocol (PTP)
[[52](ch08.html#Bigum2015ux)],
and careful deployment and monitoring. However, it requires significant effort and expertise, and
there are plenty of ways clock synchronization can go wrong. If your NTP daemon is
misconfigured, or a firewall is blocking NTP traffic, the clock error due to drift can quickly
become large. ## Relying on Synchronized Clocks 
The problem with clocks is that while they seem simple and easy to use, they have a surprising
number of pitfalls: a day may not have exactly 86,400 seconds, time-of-day clocks may move backward
in time, and the time on one node may be quite different from the time on another node. Earlier in this chapter we discussed networks dropping and arbitrarily delaying packets. Even though
networks are well behaved most of the time, software must be designed on the assumption that the
network will occasionally be faulty, and the software must handle such faults gracefully. The same
is true with clocks: although they work quite well most of the time, robust software needs to be
prepared to deal with incorrect clocks.