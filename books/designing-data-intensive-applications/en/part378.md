![ddia 0513](assets/ddia_0513.png) ###### Figure 5-13. Capturing causal dependencies between two clients concurrently editing a shopping cart. The dataflow between the operations in [Figure 5-13](#fig_replication_causality_single) is illustrated
graphically in [Figure 5-14](#fig_replication_causal_dependencies). The arrows indicate which operation
happened before which other operation, in the sense that the later operation knew about or
depended on the earlier one. In this example, the clients are never fully up to date with the data
on the server, since there is always another operation going on concurrently. But old versions of
the value do get overwritten eventually, and no writes are lost. ![ddia 0514](assets/ddia_0514.png) ###### Figure 5-14. Graph of causal dependencies in [Figure 5-13](#fig_replication_causality_single). Note that the server can determine whether two operations are concurrent by looking at the version
numbers—it does not need to interpret the value itself (so the value could be any data
structure). The algorithm works as follows: *  The server maintains a version number for every key, increments the version number every time that
key is written, and stores the new version number along with the value written.