The term “eventually” is deliberately vague: in general, there is no limit to how far a replica can
fall behind. In normal operation, the delay between a write happening on the leader and being
reflected on a follower—the replication lag—may be only a fraction of a second, and not
noticeable in practice. However, if the system is operating near capacity or if there is a problem
in the network, the lag can easily increase to several seconds or even minutes. When the lag is so large, the inconsistencies it introduces are not just a theoretical issue but a
real problem for applications. In this section we will highlight three examples of problems that are
likely to occur when there is replication lag and outline some approaches to solving them. ## Reading Your Own Writes 
Many applications let the user submit some data and then view what they have submitted. This might
be a record in a customer database, or a comment on a discussion thread, or something else of that sort.
When new data is submitted, it must be sent to the leader, but when the user views the data, it can
be read from a follower. This is especially appropriate if data is frequently viewed but only
occasionally written.