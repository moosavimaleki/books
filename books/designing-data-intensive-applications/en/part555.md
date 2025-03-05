
It may make sense to deliberately trigger network problems and test the system’s response (this is
the idea behind Chaos Monkey; see [“Reliability”](ch01.html#sec_introduction_reliability)). ## Detecting Faults 
Many systems need to automatically detect faulty nodes. For example: *  A load balancer needs to stop sending requests to a node that is dead (i.e., take it out of rotation). *  In a distributed database with single-leader replication, if the leader fails, one of the
followers needs to be promoted to be the new leader (see [“Handling Node Outages”](ch05.html#sec_replication_failover)). Unfortunately, the uncertainty about the network makes it difficult to tell whether a node is
working or not. In some specific circumstances you might get some feedback to explicitly tell you
that something is not working: *  
If you can reach the machine on which the node should be running, but no process is listening on
the destination port (e.g., because the process crashed), the operating system will helpfully close
or refuse TCP connections by sending a RST or FIN packet in reply. However, if the node
crashed while it was handling your request, you have no way of knowing how much data was actually
processed by the remote node [[22](ch08.html#Hubert2009wf)].