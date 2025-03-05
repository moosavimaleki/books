*  Mergeable persistent data structures
[[41](ch05.html#Farinier2015wj)] track history explicitly, similarly to the Git version control
system, and use a three-way merge function (whereas CRDTs use two-way merges). *  Operational transformation
[[42](ch05.html#Sun1998vf)]
is the conflict resolution algorithm behind collaborative editing applications such as Etherpad
[[30](ch05.html#AppJetInc2011um)] and Google Docs
[[31](ch05.html#DayRichter2010tt)]. It was designed particularly for
concurrent editing of an ordered list of items, such as the list of characters that constitute a
text document. Implementations of these algorithms in databases are still young, but it’s likely that they will be
integrated into more replicated data systems in the future. Automatic conflict resolution could make
multi-leader data synchronization much simpler for applications to deal with. ### What is a conflict? 
Some kinds of conflict are obvious. In the example in [Figure 5-7](#fig_replication_write_conflict), two writes
concurrently modified the same field in the same record, setting it to two different values. There
is little doubt that this is a conflict.