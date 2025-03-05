### Merging concurrently written values 
This algorithm ensures that no data is silently dropped, but it unfortunately requires that the
clients do some extra work: if several operations happen concurrently, clients have to clean up
afterward by merging the concurrently written values. Riak calls these concurrent values
siblings. Merging sibling values is essentially the same problem as conflict resolution in multi-leader
replication, which we discussed previously (see [“Handling Write Conflicts”](#sec_replication_write_conflicts)). A simple
approach is to just pick one of the values based on a version number or timestamp (last write wins),
but that implies losing data. So, you may need to do something more intelligent in application code. With the example of a shopping cart, a reasonable approach to merging siblings is to just take the
union. In [Figure 5-14](#fig_replication_causal_dependencies), the two final siblings are [milk, flour, eggs, bacon]
and [eggs, milk, ham]; note that milk and eggs appear in both, even though they were each only
written once. The merged value might be something like [milk, flour, eggs, bacon, ham], without
duplicates.