*  A runaway process that uses up some shared resource—CPU time, memory, disk space, or network
bandwidth. *  A service that the system depends on that slows down, becomes unresponsive, or starts returning
corrupted responses. *  
Cascading failures, where a small fault in one component triggers a fault in another component,
which in turn triggers further faults
[[10](ch01.html#AmazonWebServices2011tj)]. The bugs that cause these kinds of software faults often lie dormant for a long time until they are
triggered by an unusual set of circumstances. In those circumstances, it is revealed that the
software is making some kind of assumption about its environment—and while that assumption is
usually true, it eventually stops being true for some reason
[[11](ch01.html#Cook2000wo)]. There is no quick solution to the problem of systematic faults in software. Lots of small things can
help: carefully thinking about assumptions and interactions in the system; thorough testing; process
isolation; allowing processes to crash and restart; measuring, monitoring, and analyzing system
behavior in production. If a system is expected to provide some guarantee (for example, in a message
queue, that the number of incoming messages equals the number of outgoing messages), it can
constantly check itself while it is running and raise an alert if a discrepancy is found
[[12](ch01.html#Kreps2012td_ch1)].