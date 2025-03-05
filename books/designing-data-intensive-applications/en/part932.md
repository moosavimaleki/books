Like message brokers, change data capture is usually asynchronous: the system of record database
does not wait for the change to be applied to consumers before committing it. This design has the
operational advantage that adding a slow consumer does not affect the system of record too much, but it
has the downside that all the issues of replication lag apply (see [“Problems with Replication Lag”](ch05.html#sec_replication_lag)). ### Initial snapshot 
If you have the log of all changes that were ever made to a database, you can reconstruct the entire
state of the database by replaying the log. However, in many cases, keeping all changes forever
would require too much disk space, and replaying it would take too long, so the log needs to be
truncated. Building a new full-text index, for example, requires a full copy of the entire database—it is
not sufficient to only apply a log of recent changes, since it would be missing items that were not
recently updated. Thus, if you don’t have the entire log history, you need to start with a
consistent snapshot, as previously discussed in [“Setting Up New Followers”](ch05.html#sec_replication_new_replica).