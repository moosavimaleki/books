Failover can happen manually (an administrator is notified that the leader has failed and takes the
necessary steps to make a new leader) or automatically. An automatic failover process usually
consists of the following steps: 1.  Determining that the leader has failed. There are many things that could potentially go wrong:
crashes, power outages, network issues, and more. There is no foolproof way of detecting what
has gone wrong, so most systems simply use a timeout: nodes frequently bounce messages back and
forth between each other, and if a node doesn’t respond for some period of time—say, 30
seconds—it is assumed to be dead. (If the leader is deliberately taken down for planned
maintenance, this doesn’t apply.) 2.  Choosing a new leader. This could be done through an election process (where the leader is chosen by
a majority of the remaining replicas), or a new leader could be appointed by a previously elected
controller node. The best candidate for leadership is usually the replica with the most
up-to-date data changes from the old leader (to minimize any data loss). Getting all the nodes to
agree on a new leader is a consensus problem, discussed in detail in [Chapter 9](ch09.html#ch_consistency).