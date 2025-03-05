*  If a sloppy quorum is used (see [“Sloppy Quorums and Hinted Handoff”](#sec_replication_sloppy_quorum)), the w writes may end up on
different nodes than the r reads, so there is no longer a guaranteed overlap between the r
nodes and the w nodes [[46](ch05.html#Blomstedt2012vf)]. *  If two writes occur concurrently, it is not clear which one happened first. In this case, the only
safe solution is to merge the concurrent writes (see [“Handling Write Conflicts”](#sec_replication_write_conflicts)). If a
winner is picked based on a timestamp (last write wins), writes can be lost due to clock skew
[[35](ch05.html#Daily2013te_ch5)]. We will return to this topic in
[“Detecting Concurrent Writes”](#sec_replication_concurrent). *  If a write happens concurrently with a read, the write may be reflected on only some of the
replicas. In this case, it’s undetermined whether the read returns the old or the new value. *  If a write succeeded on some replicas but failed on others (for example because the disks on some
nodes are full), and overall succeeded on fewer than w replicas, it is not rolled back on the
replicas where it succeeded. This means that if a write was reported as failed, subsequent reads
may or may not return the value from that write
[[47](ch05.html#Blomstedt2012vi)].