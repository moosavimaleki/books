*  
If the application performs synchronous disk access, a thread may be paused waiting for a slow
disk I/O operation to complete [[68](ch08.html#Shaver2008ug)]. In many languages, disk access can happen
surprisingly, even if the code doesn’t explicitly mention file access—for example, the Java
classloader lazily loads class files when they are first used, which could happen at any time in
the program execution. I/O pauses and GC pauses may even conspire to combine their delays
[[69](ch08.html#Zhuang2016ui)]. If the disk is actually a network filesystem or network block device (such as
Amazon’s EBS), the I/O latency is further subject to the variability of network delays
[[29](ch08.html#Newman2012vf)]. *  
If the operating system is configured to allow swapping to disk (paging), a simple memory
access may result in a page fault that requires a page from disk to be loaded into memory. The
thread is paused while this slow I/O operation takes place. If memory pressure is high, this may
in turn require a different page to be swapped out to disk. In extreme circumstances, the
operating system may spend most of its time swapping pages in and out of memory and getting little
actual work done (this is known as thrashing). To avoid this problem, paging is often disabled
on server machines (if you would rather kill a process to free up memory than risk thrashing).