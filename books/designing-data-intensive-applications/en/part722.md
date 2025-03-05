![ddia 0910](assets/ddia_0910.png) ###### Figure 9-10. The coordinator crashes after participants vote “yes.” Database 1 does not know whether to commit or abort. Without hearing from the coordinator, the participant has no way of knowing whether to commit or
abort. In principle, the participants could communicate among themselves to find out how each
participant voted and come to some agreement, but that is not part of the 2PC protocol. The only way 2PC can complete is by waiting for the coordinator to recover. This is why the
coordinator must write its commit or abort decision to a transaction log on disk before sending
commit or abort requests to participants: when the coordinator recovers, it determines the status of
all in-doubt transactions by reading its transaction log. Any transactions that don’t have a commit
record in the coordinator’s log are aborted. Thus, the commit point of 2PC comes down to a regular
single-node atomic commit on the coordinator.