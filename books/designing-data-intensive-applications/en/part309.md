2.  Copy the snapshot to the new follower node. 3.  
The follower connects to the leader and requests all the data changes that have happened since
the snapshot was taken. This requires that the snapshot is associated with an exact position in
the leader’s replication log. That position has various names: for example, PostgreSQL calls it
the log sequence number, and MySQL calls it the binlog coordinates. 4.  When the follower has processed the backlog of data changes since the snapshot, we say it has
caught up. It can now continue to process data changes from the leader as they happen. The practical steps of setting up a follower vary significantly by database. In some systems the
process is fully automated, whereas in others it can be a somewhat arcane multi-step workflow that
needs to be manually performed by an administrator. ## Handling Node Outages 
Any node in the system can go down, perhaps unexpectedly due to a fault, but just as likely due to
planned maintenance (for example, rebooting a machine to install a kernel security patch). Being
able to reboot individual nodes without downtime is a big advantage for operations and maintenance.
Thus, our goal is to keep the system as a whole running despite individual node failures, and to keep
the impact of a node outage as small as possible.