
With asynchronous replication, there is a problem, illustrated in
[Figure 5-3](#fig_replication_read_your_writes): if the user views the data shortly after making a write, the
new data may not yet have reached the replica. To the user, it looks as though the data they
submitted was lost, so they will be understandably unhappy. ![ddia 0503](assets/ddia_0503.png) ###### Figure 5-3. A user makes a write, followed by a read from a stale replica. To prevent this anomaly, we need read-after-write consistency. 
In this situation, we need read-after-write consistency, also known as read-your-writes consistency
[[24](ch05.html#Terry1994fp)].
This is a guarantee that if the user reloads the page, they will always see any updates they
submitted themselves. It makes no promises about other users: other users’ updates may not be
visible until some later time. However, it reassures the user that their own input has been saved
correctly. How can we implement read-after-write consistency in a system with leader-based replication? There
are various possible techniques. To mention a few: