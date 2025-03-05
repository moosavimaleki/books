
In [“Describing Load”](ch01.html#sec_introduction_scalability_load) we discussed Twitter’s home timelines, a cache of
recently written tweets by the people a particular user is following (like a mailbox). This is
another example of read-optimized state: home timelines are highly denormalized, since your tweets
are duplicated in all of the timelines of the people following you. However, the fan-out service
keeps this duplicated state in sync with new tweets and new following relationships, which keeps the
duplication manageable. ### Concurrency control 
The biggest downside of event sourcing and change data capture is that the consumers of the event
log are usually asynchronous, so there is a possibility that a user may make a write to the log,
then read from a log-derived view and find that their write has not yet been reflected in the read
view. We discussed this problem and potential solutions previously in [“Reading Your Own Writes”](ch05.html#sec_replication_ryw). One solution would be to perform the updates of the read view synchronously with appending the event
to the log. This requires a transaction to combine the writes into an atomic unit, so either you
need to keep the event log and the read view in the same storage system, or you need a distributed
transaction across the different systems. Alternatively, you could use the approach discussed in
[“Implementing linearizable storage using total order broadcast”](ch09.html#sec_consistency_abcast_to_lin).