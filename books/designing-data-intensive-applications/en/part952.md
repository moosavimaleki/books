### Limitations of immutability 
Many systems that don’t use an event-sourced model nevertheless rely on immutability: various
databases internally use immutable data structures or multi-version data to support point-in-time
snapshots (see [“Indexes and snapshot isolation”](ch07.html#sec_transactions_snapshot_indexes)). Version control systems such as Git,
Mercurial, and Fossil also rely on immutable data to preserve version history of files. 
To what extent is it feasible to keep an immutable history of all changes forever? The answer
depends on the amount of churn in the dataset. Some workloads mostly add data and rarely update or
delete; they are easy to make immutable. Other workloads have a high rate of updates and deletes on
a comparatively small dataset; in these cases, the immutable history may grow prohibitively large,
fragmentation may become an issue, and the performance of compaction and garbage collection becomes
crucial for operational robustness [[60](ch11.html#Schwartz2013ur_ch11),
[61](ch11.html#Eloff2015xu)]. 
Besides the performance reasons, there may also be circumstances in which you need data to be
deleted for administrative reasons, in spite of all immutability. For example, privacy regulations
may require deleting a user’s personal information after they close their account, data protection
legislation may require erroneous information to be removed, or an accidental leak of sensitive
information may need to be contained.