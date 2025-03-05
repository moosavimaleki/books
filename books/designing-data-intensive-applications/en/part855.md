# Beyond MapReduce Although MapReduce became very popular and received a lot of hype in the late 2000s, it is just one
among many possible programming models for distributed systems. Depending on the volume of data, the
structure of the data, and the type of processing being done with it, other tools may be more
appropriate for expressing a computation. 
We nevertheless spent a lot of time in this chapter discussing MapReduce because it is a useful
learning tool, as it is a fairly clear and simple abstraction on top of a distributed filesystem.
That is, simple in the sense of being able to understand what it is doing, not in the sense of
being easy to use. Quite the opposite: implementing a complex processing job using the raw MapReduce
APIs is actually quite hard and laborious—for instance, you would need to implement any join
algorithms from scratch [[37](ch10.html#Grover2015tl)]. 
In response to the difficulty of using MapReduce directly, various higher-level programming models
(Pig, Hive, Cascading, Crunch) were created as abstractions on top of MapReduce. If you understand
how MapReduce works, they are fairly easy to learn, and their higher-level constructs make many
common batch processing tasks significantly easier to implement.