The simplest approach for avoiding hot spots would be to assign records to nodes randomly. That would
distribute the data quite evenly across the nodes, but it has a big disadvantage: when you’re trying to
read a particular item, you have no way of knowing which node it is on, so you have to query
all nodes in parallel. We can do better. Let’s assume for now that you have a simple key-value data model, in which you
always access a record by its primary key. For example, in an old-fashioned paper encyclopedia, you
look up an entry by its title; since all the entries are alphabetically sorted by title, you can
quickly find the one you’re looking for. ## Partitioning by Key Range 
One way of partitioning is to assign a continuous range of keys (from some minimum to some maximum)
to each partition, like the volumes of a paper encyclopedia ([Figure 6-2](#fig_partitioning_encyclopedia)). If
you know the boundaries between the ranges, you can easily determine which partition contains a
given key. If you also know which partition is assigned to which node, then you can make your
request directly to the appropriate node (or, in the case of the encyclopedia, pick the correct book
off the shelf).