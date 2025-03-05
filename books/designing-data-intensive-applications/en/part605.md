
If a node continues acting as the chosen one, even though the majority of nodes have declared it
dead, it could cause problems in a system that is not carefully designed. Such a node could send
messages to other nodes in its self-appointed capacity, and if other nodes believe it, the system as
a whole may do something incorrect. 
For example, [Figure 8-4](#fig_distributed_io_fencing) shows a data corruption bug due to an incorrect
implementation of locking. (The bug is not theoretical: HBase used to have this problem
[[74](ch08.html#Junqueira2013wi_ch8), [75](ch08.html#Soztutar2013vj)].) Say you want to ensure that a file in a storage service can only be
accessed by one client at a time, because if multiple clients tried to write to it, the file would
become corrupted. You try to implement this by requiring a client to obtain a lease from a lock
service before accessing the file. ![ddia 0804](assets/ddia_0804.png) ###### Figure 8-4. Incorrect implementation of a distributed lock: client 1 believes that it still has a valid lease, even though it has expired, and thus corrupts a file in storage.