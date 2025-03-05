Now, if a node is added to the cluster, the new node can steal a few partitions from every
existing node until partitions are fairly distributed once again. This process is illustrated in
[Figure 6-6](#fig_partitioning_rebalance_fixed). If a node is removed from the cluster, the same happens in
reverse. Only entire partitions are moved between nodes. The number of partitions does not change, nor does
the assignment of keys to partitions. The only thing that changes is the assignment of
partitions to nodes. This change of assignment is not immediate—it takes some time to transfer a
large amount of data over the network—so the old assignment of partitions is used for any reads
and writes that happen while the transfer is in progress. ![ddia 0606](assets/ddia_0606.png) ###### Figure 6-6. Adding a new node to a database cluster with multiple partitions per node. In principle, you can even account for mismatched hardware in your cluster: by assigning more
partitions to nodes that are more powerful, you can force those nodes to take a greater share of the
load.