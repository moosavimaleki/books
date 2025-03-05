
Until recently, redundancy of hardware components was sufficient for most applications, since it
makes total failure of a single machine fairly rare. As long as you can restore a backup onto a new
machine fairly quickly, the downtime in case of failure is not catastrophic in most applications.
Thus, multi-machine redundancy was only required by a small number of applications for which high
availability was absolutely essential. 
However, as data volumes and applications’ computing demands have increased, more applications have begun using
larger numbers of machines, which proportionally increases the rate of hardware faults. Moreover, in
some cloud platforms such as Amazon Web Services (AWS) it is fairly common for virtual machine instances
to become unavailable without warning [[7](ch01.html#Voss2012tc)], as the platforms are designed to
prioritize flexibility and elasticity[i](ch01.html#idm140605786161136)
over single-machine reliability. 
Hence there is a move toward systems that can tolerate the loss of entire machines, by using
software fault-tolerance techniques in preference or in addition to hardware redundancy. Such
systems also have operational advantages: a single-server system requires planned downtime if you
need to reboot the machine (to apply operating system security patches, for example), whereas a
system that can tolerate machine failure can be patched one node at a time, without downtime of the
entire system (a rolling upgrade; see [Chapter 4](ch04.html#ch_encoding)).