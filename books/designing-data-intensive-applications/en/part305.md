The diagram shows that there is a substantial delay before follower 2 processes the message.
Normally, replication is quite fast: most database systems apply changes to followers in less than a
second. However, there is no guarantee of how long it might take. There are circumstances when
followers might fall behind the leader by several minutes or more; for example, if a follower is
recovering from a failure, if the system is operating near maximum capacity, or if there are network
problems between the nodes. The advantage of synchronous replication is that the follower is guaranteed to have an up-to-date
copy of the data that is consistent with the leader. If the leader suddenly fails, we can be sure
that the data is still available on the follower. The disadvantage is that if the synchronous
follower doesn’t respond (because it has crashed, or there is a network fault, or for any other
reason), the write cannot be processed. The leader must block all writes and wait until the
synchronous replica is available again.