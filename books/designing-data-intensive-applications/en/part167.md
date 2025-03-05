Even though there are many subtleties, the basic idea of LSM-trees—keeping a cascade of SSTables
that are merged in the background—is simple and effective. Even when the dataset is much bigger
than the available memory it continues to work well. Since data is stored in sorted order, you can efficiently
perform range queries (scanning all keys above some minimum and up to some maximum), and because the
disk writes are sequential the LSM-tree can support remarkably high write throughput. ## B-Trees 
The log-structured indexes we have discussed so far are gaining acceptance, but they are not the
most common type of index. The most widely used indexing structure is quite different: the B-tree. 
Introduced in 1970 [[17](ch03.html#Bayer1970tq)] and called “ubiquitous” less than 10 years later
[[18](ch03.html#Comer1979uy)],
B-trees have stood the test of time very well. They remain the standard index implementation in
almost all relational databases, and many nonrelational databases use them too.