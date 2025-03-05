However, if you want to allow people to also remove things from their carts, and not just add
things, then taking the union of siblings may not yield the right result: if you merge two sibling
carts and an item has been removed in only one of them, then the removed item will reappear in the
union of the siblings [[37](ch05.html#DeCandia2007ui_ch5)]. To prevent
this problem, an item cannot simply be deleted from the database when it is removed; instead, the
system must leave a marker with an appropriate version number to indicate that the item has been
removed when merging siblings.  Such a deletion marker is known as a tombstone.
(We previously saw tombstones in the context of log compaction in [“Hash Indexes”](ch03.html#sec_storage_hash_index).) 
As merging siblings in application code is complex and error-prone, there are some efforts to design
data structures that can perform this merging automatically, as discussed in
[“Automatic Conflict Resolution”](#sidebar_conflict_resolution). For example, Riak’s datatype support uses a family of data
structures called CRDTs [[38](ch05.html#Shapiro2011wy),
[39](ch05.html#Elliott2013ua),
[55](ch05.html#Jacobson2014wa_ch5)] that can automatically merge siblings in sensible
ways, including preserving deletions.