### Implementing linearizable storage using total order broadcast 
As illustrated in [Figure 9-4](#fig_consistency_linearizability_3), in a linearizable system there is a total
order of operations. Does that mean linearizability is the same as total order broadcast? Not quite,
but there are close links between the two.[x](ch09.html#idm140605759439152) Total order broadcast is asynchronous: messages are guaranteed to be delivered reliably in a fixed
order, but there is no guarantee about when a message will be delivered (so one recipient may lag
behind the others). By contrast, linearizability is a recency guarantee: a read is guaranteed to see
the latest value written. However, if you have total order broadcast, you can build linearizable storage on top of it. For
example, you can ensure that usernames uniquely identify user accounts. Imagine that for every possible username, you can have a linearizable register with an atomic
compare-and-set operation. Every register initially has the value null (indicating that the
username is not taken). When a user wants to create a username, you execute a compare-and-set
operation on the register for that username, setting it to the user account ID, under the condition
that the previous register value is null. If multiple users try to concurrently grab the same
username, only one of the compare-and-set operations will succeed, because the others will see a
value other than null (due to linearizability).