This nondeterminism and possibility of partial failures is what makes distributed systems hard to
work with [[5](ch08.html#Hodges2013tj)]. ## Cloud Computing and Supercomputing 
There is a spectrum of philosophies on how to build large-scale computing systems: *  
At one end of the scale is the field of high-performance computing (HPC). Supercomputers
with thousands of CPUs are typically used for computationally intensive scientific computing
tasks, such as weather forecasting or molecular dynamics (simulating the movement of atoms and
molecules). *  
At the other extreme is cloud computing, which is not very well defined
[[6](ch08.html#Regalado2011vn)]
but is often associated with multi-tenant datacenters, commodity computers connected with an IP
network (often Ethernet), elastic/on-demand resource allocation, and metered billing. *  Traditional enterprise datacenters lie somewhere between these extremes. 
With these philosophies come very different approaches to handling faults. In a supercomputer, a job
typically checkpoints the state of its computation to durable storage from time to time. If one node
fails, a common solution is to simply stop the entire cluster workload. After the faulty node is
repaired, the computation is restarted from the last checkpoint
[[7](ch08.html#Barroso2013ba),
[8](ch08.html#Fiala2012ti)].
Thus, a supercomputer is more like a single-node computer than a distributed system: it deals with
partial failure by letting it escalate into total failure—if any part of the system fails, just
let everything crash (like a kernel panic on a single machine).