![ddia 0504](assets/ddia_0504.png) ###### Figure 5-4. A user first reads from a fresh replica, then from a stale replica. Time appears to go backward. To prevent this anomaly, we need monotonic reads. Monotonic reads [[23](ch05.html#Terry2011vp)] is a guarantee that this
kind of anomaly does not happen. It’s a lesser guarantee than strong consistency, but a stronger
guarantee than eventual consistency. When you read data, you may see an old value; monotonic reads
only means that if one user makes several reads in sequence, they will not see time go
backward—i.e., they will not read older data after having previously read newer data. One way of achieving monotonic reads is to make sure that each user always makes their reads from
the same replica (different users can read from different replicas). For example, the replica can be
chosen based on a hash of the user ID, rather than randomly. However, if that replica fails, the
user’s queries will need to be rerouted to another replica.