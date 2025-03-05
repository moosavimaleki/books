*  In a geographically distributed deployment (keeping data geographically close to your users to
reduce access latency), communication most likely goes over the internet, which is slow and
unreliable compared to local networks. Supercomputers generally assume that all of their nodes are
close together. 
If we want to make distributed systems work, we must accept the possibility of partial failure and
build fault-tolerance mechanisms into the software. In other words, we need to build a reliable
system from unreliable components. (As discussed in [“Reliability”](ch01.html#sec_introduction_reliability), there is no
such thing as perfect reliability, so we’ll need to understand the limits of what we can
realistically promise.) Even in smaller systems consisting of only a few nodes, it’s important to think about partial
failure. In a small system, it’s quite likely that most of the components are working correctly most
of the time. However, sooner or later, some part of the system will become faulty, and the
software will have to somehow handle it. The fault handling must be part of the software design, and
you (as operator of the software) need to know what behavior to expect from the software in the case
of a fault.