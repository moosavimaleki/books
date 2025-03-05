
When we think of causes of system failure, hardware faults quickly come to mind. Hard disks crash,
RAM becomes faulty, the power grid has a blackout, someone unplugs the wrong network cable. Anyone
who has worked with large datacenters can tell you that these things happen all the time when you
have a lot of machines. Hard disks are reported as having a mean time to failure (MTTF) of about 10 to 50 years
[[5](ch01.html#Ford2010vv), [6](ch01.html#Beach2014ui)].
Thus, on a storage cluster with 10,000 disks, we should expect on average one disk to die per day. 
Our first response is usually to add redundancy to the individual hardware components in order to
reduce the failure rate of the system. Disks may be set up in a RAID configuration, servers may have
dual power supplies and hot-swappable CPUs, and datacenters may have batteries and diesel
generators for backup power. When one component dies, the redundant component can take its place
while the broken component is replaced. This approach cannot completely prevent hardware problems
from causing failures, but it is well understood and can often keep a machine running uninterrupted
for years.