
The techniques for determining which operation happened before which other operation are similar to
what we discussed in [“Detecting Concurrent Writes”](ch05.html#sec_replication_concurrent). That section discussed causality in a
leaderless datastore, where we need to detect concurrent writes to the same key in order to prevent
lost updates. Causal consistency goes further: it needs to track causal dependencies across the
entire database, not just for a single key. Version vectors can be generalized to do this
[[54](ch09.html#Goncalves2015ky)]. 
In order to determine the causal ordering, the database needs to know which version of the data was
read by the application. This is why, in [Figure 5-13](ch05.html#fig_replication_causality_single), the version number
from the prior operation is passed back to the database on a write. A similar idea appears in the
conflict detection of SSI, as discussed in [“Serializable Snapshot Isolation (SSI)”](ch07.html#sec_transactions_ssi):
when a transaction wants to commit, the database checks whether the version of the data that it read
is still up to date. To this end, the database keeps track of which data has been read by which
transaction.