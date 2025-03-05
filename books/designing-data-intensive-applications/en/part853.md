
To understand the reasons for MapReduce’s sparing use of memory and task-level recovery, it is
helpful to look at the environment for which MapReduce was originally designed. Google has mixed-use
datacenters, in which online production services and offline batch jobs run on the same machines.
Every task has a resource allocation (CPU cores, RAM, disk space, etc.) that is enforced using
containers. Every task also has a priority, and if a higher-priority task needs more resources,
lower-priority tasks on the same machine can be terminated (preempted) in order to free up
resources. Priority also determines pricing of the computing resources: teams must pay for the
resources they use, and higher-priority processes cost more
[[59](ch10.html#Verma2015gi)]. This architecture allows non-production (low-priority) computing resources to be overcommitted,
because the system knows that it can reclaim the resources if necessary. Overcommitting resources in
turn allows better utilization of machines and greater efficiency compared to systems that segregate
production and non-production tasks. However, as MapReduce jobs run at low priority, they run the
risk of being preempted at any time because a higher-priority process requires their resources.
Batch jobs effectively “pick up the scraps under the table,” using any computing resources that
remain after the high-priority processes have taken what they need.