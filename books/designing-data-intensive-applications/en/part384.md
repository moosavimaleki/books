# Summary In this chapter we looked at the issue of replication. Replication can serve several purposes: *High availability* Keeping the system running, even when one machine (or several machines, or an
entire datacenter) goes down *Disconnected operation* Allowing an application to continue working when there is a network
interruption *Latency* Placing data geographically close to users, so that users can interact with it faster *Scalability* Being able to handle a higher volume of reads than a single machine could handle,
by performing reads on replicas Despite being a simple goal—keeping a copy of the same data on several machines—replication turns out
to be a remarkably tricky problem. It requires carefully thinking about concurrency and about all
the things that can go wrong, and dealing with the consequences of those faults. At a minimum, we
need to deal with unavailable nodes and network interruptions (and that’s not even considering the
more insidious kinds of fault, such as silent data corruption due to software bugs).