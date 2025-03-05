Replication can be synchronous or asynchronous, which has a profound effect on the system behavior
when there is a fault. Although asynchronous replication can be fast when the system is running
smoothly, it’s important to figure out what happens when replication lag increases and servers fail.
If a leader fails and you promote an asynchronously updated follower to be the new leader, recently
committed data may be lost. We looked at some strange effects that can be caused by replication lag, and we discussed a few
consistency models which are helpful for deciding how an application should behave under replication
lag: *Read-after-write consistency* Users should always see data that they submitted themselves. *Monotonic reads* After users have seen the data at one point in time, they shouldn’t later see
the data from some earlier point in time. *Consistent prefix reads* Users should see the data in a state that makes causal sense:
for example, seeing a question and its reply in the correct order.