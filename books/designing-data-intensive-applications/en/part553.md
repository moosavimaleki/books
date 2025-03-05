
Public cloud services such as EC2 are notorious for having frequent transient network glitches
[[14](ch08.html#Bailis2014jx)], and well-managed private datacenter
networks can be stabler environments. Nevertheless, nobody is immune from network problems: for
example, a problem during a software upgrade for a switch could trigger a network topology
reconfiguration, during which network packets could be delayed for more than a minute
[[17](ch08.html#Imbriaco2012tx_ch8)]. Sharks might bite undersea cables and damage them
[[18](ch08.html#Oremus2014ty)].
Other surprising faults include a network interface that sometimes drops all inbound packets but
sends outbound packets successfully [[19](ch08.html#Donges2012tt)]:
just because a network link works in one direction doesn’t guarantee it’s also working in the
opposite direction. # Network partitions 
When one part of the network is cut off from the rest due to a network fault, that is sometimes
called a network partition or netsplit. In this book we’ll generally stick with the more general term
network fault, to avoid confusion with partitions (shards) of a storage system, as discussed in
[Chapter 6](ch06.html#ch_partitioning).