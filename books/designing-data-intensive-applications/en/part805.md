
Various other distributed filesystems besides HDFS exist, such as GlusterFS and the Quantcast File System (QFS)
[[20](ch10.html#Ovsiannikov2013da)].
Object storage services such as Amazon S3, Azure Blob Storage, and OpenStack Swift
[[21](ch10.html#OpenStackSwift)]
are similar in many ways.[iv](ch10.html#idm140605758239072)
In this chapter we will mostly use HDFS as a running example, but the principles apply to any
distributed filesystem. 
HDFS is based on the shared-nothing principle (see the introduction to [Part II](part02.html#part_distributed_data)), in
contrast to the shared-disk approach of Network Attached Storage (NAS) and Storage Area Network
(SAN) architectures. Shared-disk storage is implemented by a centralized storage appliance, often
using custom hardware and special network infrastructure such as Fibre Channel. On the other hand,
the shared-nothing approach requires no special hardware, only computers connected by a conventional
datacenter network. 
HDFS consists of a daemon process running on each machine, exposing a network service that allows
other nodes to access files stored on that machine (assuming that every general-purpose machine in a
datacenter has some disks attached to it). A central server called the NameNode keeps track of which
file blocks are stored on which machine. Thus, HDFS conceptually creates one big filesystem that can
use the space on the disks of all machines running the daemon.