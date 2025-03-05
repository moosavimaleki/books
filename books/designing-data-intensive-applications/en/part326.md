*  
The client can remember the timestamp of its most recent write—then the system can ensure that the
replica serving any reads for that user reflects updates at least until that timestamp. If a
replica is not sufficiently up to date, either the read can be handled by another replica or the
query can wait until the replica has caught up.

The timestamp could be a logical timestamp (something that indicates ordering of writes, such as
the log sequence number) or the actual system clock (in which case clock synchronization becomes
critical; see [“Unreliable Clocks”](ch08.html#sec_distributed_clocks)). *  
If your replicas are distributed across multiple datacenters (for geographical proximity to users
or for availability), there is additional complexity. Any request that needs to be served by the
leader must be routed to the datacenter that contains the leader. 
Another complication arises when the same user is accessing your service from multiple devices, for
example a desktop web browser and a mobile app. In this case you may want to provide cross-device
read-after-write consistency: if the user enters some information on one device and then views it
on another device, they should see the information they just entered.