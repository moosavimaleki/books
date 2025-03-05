
In these circumstances, it’s not sufficient to just append another event to the log to indicate that
the prior data should be considered deleted—you actually want to rewrite history and pretend that
the data was never written in the first place. For example, Datomic calls this feature excision
[[62](ch11.html#DatomicExcision)], and the Fossil
version control system has a similar concept called shunning
[[63](ch11.html#FossilShun)]. Truly deleting data is surprisingly hard [[64](ch11.html#Kreps2015zt)], since copies can live in many places: for example, storage engines, filesystems, and
SSDs often write to a new location rather than overwriting in place
[[52](ch11.html#Helland2015vx)], and backups are often deliberately
immutable to prevent accidental deletion or corruption. Deletion is more a matter of “making it
harder to retrieve the data” than actually “making it impossible to retrieve the data.”
Nevertheless, you sometimes have to try, as we shall see in [“Legislation and self-regulation”](ch12.html#sec_future_legislation). # Processing Streams 
So far in this chapter we have talked about where streams come from (user activity events, sensors,
and writes to databases), and we have talked about how streams are transported (through direct
messaging, via message brokers, and in event logs).