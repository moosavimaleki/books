There are various ways of achieving convergent conflict resolution: *  
Give each write a unique ID (e.g., a timestamp, a long random number, a UUID, or a hash of the key
and value), pick the write with the highest ID as the winner, and throw away the other writes.
If a timestamp is used, this technique is known as last write wins (LWW). Although this approach
is popular, it is dangerously prone to data loss
[[35](ch05.html#Daily2013te_ch5)].
We will discuss LWW in more detail at the end of this chapter ([“Detecting Concurrent Writes”](#sec_replication_concurrent)). *  Give each replica a unique ID, and let writes that originated at a higher-numbered replica
always take precedence over writes that originated at a lower-numbered replica. This approach also implies
data loss. *  Somehow merge the values together—e.g., order them alphabetically and then concatenate them (in
[Figure 5-7](#fig_replication_write_conflict), the merged title might be something like “B/C”). * 