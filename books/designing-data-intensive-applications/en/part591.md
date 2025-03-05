
However, what if there is an unexpected pause in the execution of the program? For example, imagine
the thread stops for 15 seconds around the line lease.isValid() before finally continuing. In
that case, it’s likely that the lease will have expired by the time the request is processed, and
another node has already taken over as leader. However, there is nothing to tell this thread that it
was paused for so long, so this code won’t notice that the lease has expired until the next
iteration of the loop—by which time it may have already done something unsafe by processing the
request. 
Is it crazy to assume that a thread might be paused for so long? Unfortunately not. There are
various reasons why this could happen: *  
Many programming language runtimes (such as the Java Virtual Machine) have a garbage collector
(GC) that occasionally needs to stop all running threads. These “stop-the-world” GC pauses have
sometimes been known to last for several minutes [[64](ch08.html#Lipcon2011tn)]!
Even so-called “concurrent” garbage collectors like the HotSpot JVM’s CMS cannot fully run in
parallel with the application code—even they need to stop the world from time to time
[[65](ch08.html#Thompson2013vj)].
Although the pauses can often be reduced by changing allocation patterns or tuning GC settings
[[66](ch08.html#Ragozin2011wr)],
we must assume the worst if we want to offer robust guarantees.