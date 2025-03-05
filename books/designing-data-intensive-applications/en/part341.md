### Conflict avoidance 
The simplest strategy for dealing with conflicts is to avoid them: if the application can ensure
that all writes for a particular record go through the same leader, then conflicts cannot occur.
Since many implementations of multi-leader replication handle conflicts quite poorly, avoiding
conflicts is a frequently recommended approach
[[34](ch05.html#Hodges2013vb)]. For example, in an application where a user can edit their own data, you can ensure that requests
from a particular user are always routed to the same datacenter and use the leader in that
datacenter for reading and writing. Different users may have different “home” datacenters (perhaps
picked based on geographic proximity to the user), but from any one user’s point of view the
configuration is essentially single-leader. However, sometimes you might want to change the designated leader for a record—perhaps because
one datacenter has failed and you need to reroute traffic to another datacenter, or perhaps because
a user has moved to a different location and is now closer to a different datacenter. In this
situation, conflict avoidance breaks down, and you have to deal with the possibility of concurrent
writes on different leaders.