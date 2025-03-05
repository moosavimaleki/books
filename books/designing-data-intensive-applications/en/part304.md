Think about what happens in [Figure 5-1](#fig_replication_leader_follower), where the user of a website updates
their profile image. At some point in time, the client sends the update request to the leader;
shortly afterward, it is received by the leader. At some point, the leader forwards the data change
to the followers. Eventually, the leader notifies the client that the update was successful. [Figure 5-2](#fig_replication_sync_replication) shows the communication between various components of the
system: the user’s client, the leader, and two followers. Time flows from left to right. A request
or response message is shown as a thick arrow. ![ddia 0502](assets/ddia_0502.png) ###### Figure 5-2. Leader-based replication with one synchronous and one asynchronous follower. 
In the example of [Figure 5-2](#fig_replication_sync_replication), the replication to follower 1 is
synchronous: the leader waits until follower 1 has confirmed that it received the write before
reporting success to the user, and before making the write visible to other clients. The replication
to follower 2 is asynchronous: the leader sends the message, but doesn’t wait for a response from
the follower.