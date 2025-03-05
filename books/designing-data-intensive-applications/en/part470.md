
Snapshot isolation is a popular feature: it is supported by PostgreSQL, MySQL with the InnoDB
storage engine, Oracle, SQL Server, and others
[[23](ch07.html#Kleppmann2014ut),
[31](ch07.html#Momjian2014vg), [32](ch07.html#Gurusami2013ut)]. ### Implementing snapshot isolation 
Like read committed isolation, implementations of snapshot isolation typically use write locks to prevent
dirty writes (see [“Implementing read committed”](#sec_transactions_read_committed_impl)), which means that a transaction that
makes a write can block the progress of another transaction that writes to the same object. However,
reads do not require any locks. From a performance point of view, a key principle of snapshot
isolation is readers never block writers, and writers never block readers. This allows a database
to handle long-running read queries on a consistent snapshot at the same time as processing writes
normally, without any lock contention between the two. 
To implement snapshot isolation, databases use a generalization of the mechanism we saw for
preventing dirty reads in [Figure 7-4](#fig_transactions_read_committed). The database must potentially keep
several different committed versions of an object, because various in-progress transactions may need
to see the state of the database at different points in time. Because it maintains several versions
of an object side by side, this technique is known as multi-version concurrency control (MVCC).