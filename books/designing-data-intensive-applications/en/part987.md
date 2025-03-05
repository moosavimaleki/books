
The state handling in Storm’s Trident is based on a similar idea
[[78](ch11.html#StormDocs)]. Relying on idempotence implies several
assumptions: restarting a failed task must replay the same messages in the same order (a log-based
message broker does this), the processing must be deterministic, and no other node may concurrently
update the same value [[98](ch11.html#Kreps2014zt), [99](ch11.html#Elnozahy2002fp)]. 
When failing over from one processing node to another, fencing may be required (see
[“The leader and the lock”](ch08.html#sec_distributed_lock_fencing)) to prevent interference from a node that is thought to be dead but
is actually alive. Despite all those caveats, idempotent operations can be an effective way of
achieving exactly-once semantics with only a small overhead. ### Rebuilding state after a failure 
Any stream process that requires state—for example, any windowed aggregations (such as counters,
averages, and histograms) and any tables and indexes used for joins—must ensure that this state
can be recovered after a failure.