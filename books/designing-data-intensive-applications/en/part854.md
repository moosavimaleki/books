
At Google, a MapReduce task that runs for an hour has an approximately 5% risk of being terminated
to make space for a higher-priority process. This rate is more than an order of magnitude higher
than the rate of failures due to hardware issues, machine reboot, or other reasons
[[59](ch10.html#Verma2015gi)]. At this rate of preemptions, if a job has
100 tasks that each run for 10 minutes, there is a risk greater than 50% that at least one task will be
terminated before it is finished. And this is why MapReduce is designed to tolerate frequent unexpected task termination: it’s not
because the hardware is particularly unreliable, it’s because the freedom to arbitrarily terminate
processes enables better resource utilization in a computing cluster. 
Among open source cluster schedulers, preemption is less widely used. YARN’s CapacityScheduler
supports preemption for balancing the resource allocation of different queues
[[58](ch10.html#Vavilapalli2013eu)],
but general priority preemption is not supported in YARN, Mesos, or Kubernetes at the time of writing
[[60](ch10.html#Schwarzkopf2016un)].
In an environment where tasks are not so often terminated, the design decisions of MapReduce make
less sense. In the next section, we will look at some alternatives to MapReduce that make different
design decisions.