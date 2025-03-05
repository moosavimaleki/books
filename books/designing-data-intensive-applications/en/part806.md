
In order to tolerate machine and disk failures, file blocks are replicated on multiple machines.
Replication may mean simply several copies of the same data on multiple machines, as in
[Chapter 5](ch05.html#ch_replication), or an erasure coding scheme such as Reed–Solomon codes, which allows lost data
to be recovered with lower storage overhead than full replication
[[20](ch10.html#Ovsiannikov2013da),
[22](ch10.html#Zhang2015vi)].
The techniques are similar to RAID, which provides redundancy across several disks attached to the
same machine; the difference is that in a distributed filesystem, file access and replication are
done over a conventional datacenter network without special hardware. HDFS has scaled well: at the time of writing, the biggest HDFS deployments run on tens of thousands
of machines, with combined storage capacity of hundreds of petabytes
[[23](ch10.html#Cnudde2016tm)]. Such large scale has become viable because the
cost of data storage and access on HDFS, using commodity hardware and open source software, is much
lower than that of the equivalent capacity on a dedicated storage appliance
[[24](ch10.html#Baldeschwieler2012ue)].