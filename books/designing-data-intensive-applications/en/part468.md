
This anomaly is called a nonrepeatable read or read skew: if Alice were to read the balance of
account 1 again at the end of the transaction, she would see a different value ($600) than she saw
in her previous query. Read skew is considered acceptable under read committed isolation: the
account balances that Alice saw were indeed committed at the time when she read them. ###### Note 
The term skew is unfortunately overloaded: we previously used it in the sense of an unbalanced
workload with hot spots (see [“Skewed Workloads and Relieving Hot Spots”](ch06.html#sec_partitioning_skew)), whereas here it means timing anomaly. In Alice’s case, this is not a lasting problem, because she will most likely see consistent account
balances if she reloads the online banking website a few seconds later. However, some situations
cannot tolerate such temporary inconsistency: Backups 
Taking a backup requires making a copy of the entire database, which may take hours on a large
database. During the time that the backup process is running, writes will continue to be made to
the database. Thus, you could end up with some parts of the backup containing an older version of
the data, and other parts containing a newer version. If you need to restore from such a backup,
the inconsistencies (such as disappearing money) become permanent.