Membership/coordination service Given a failure detector (e.g., timeouts), the system must decide which nodes are alive, and
which should be considered dead because their sessions timed out. Uniqueness constraint 
When several transactions concurrently try to create conflicting records with the same key, the
constraint must decide which one to allow and which should fail with a constraint violation. All of these are straightforward if you only have a single node, or if you are willing to assign the
decision-making capability to a single node. This is what happens in a single-leader database: all
the power to make decisions is vested in the leader, which is why such databases are able to provide
linearizable operations, uniqueness constraints, a totally ordered replication log, and more. However, if that single leader fails, or if a network interruption makes the leader unreachable,
such a system becomes unable to make any progress. There are three ways of handling that situation: