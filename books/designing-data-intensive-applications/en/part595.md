A node in a distributed system must assume that its execution can be paused for a significant length
of time at any point, even in the middle of a function. During the pause, the rest of the world
keeps moving and may even declare the paused node dead because it’s not responding. Eventually,
the paused node may continue running, without even noticing that it was asleep until it checks its
clock sometime later. ### Response time guarantees 
In many programming languages and operating systems, threads and processes may pause for an
unbounded amount of time, as discussed. Those reasons for pausing can be eliminated if you try
hard enough. 
Some software runs in environments where a failure to respond within a specified time can cause
serious damage: computers that control aircraft, rockets, robots, cars, and other physical objects
must respond quickly and predictably to their sensor inputs. In these systems, there is a specified
deadline by which the software must respond; if it doesn’t meet the deadline, that may cause a
failure of the entire system. These are so-called hard real-time systems.