### Converging toward a consistent state 
A single-leader database applies writes in a sequential order: if there are several updates to the
same field, the last write determines the final value of the field. In a multi-leader configuration, there is no defined ordering of writes, so it’s not clear what the
final value should be. In [Figure 5-7](#fig_replication_write_conflict), at leader 1 the title is first updated
to B and then to C; at leader 2 it is first updated to C and then to B. Neither order is “more
correct” than the other. If each replica simply applied writes in the order that it saw the writes, the database would end up
in an inconsistent state: the final value would be C at leader 1 and B at leader 2. That is not
acceptable—every replication scheme must ensure that the data is eventually the same in all
replicas. Thus, the database must resolve the conflict in a convergent way, which means that all
replicas must arrive at the same final value when all changes have been replicated.