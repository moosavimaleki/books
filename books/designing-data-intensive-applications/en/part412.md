[Figure 6-5](#fig_partitioning_secondary_by_term) illustrates what this could look like: red cars from all
partitions appear under color:red in the index, but the index is partitioned so that colors
starting with the letters a to r appear in partition 0 and colors starting with s to z appear
in partition 1. The index on the make of car is partitioned similarly (with the partition boundary
being between f and h). We call this kind of index term-partitioned, because the term we’re looking for determines the partition
of the index. Here, a term would be color:red, for example. The name term comes from full-text
indexes (a particular kind of secondary index), where the terms are all the words that occur in a
document. As before, we can partition the index by the term itself, or using a hash of the term. Partitioning
by the term itself can be useful for range scans (e.g., on a numeric property, such as the asking
price of the car), whereas partitioning on a hash of the term gives a more even distribution of
load.