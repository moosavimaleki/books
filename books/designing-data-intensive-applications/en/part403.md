## Partitioning by Hash of Key 
Because of this risk of skew and hot spots, many distributed datastores use a hash function to
determine the partition for a given key. A good hash function takes skewed data and makes it uniformly distributed. Say you have a 32-bit
hash function that takes a string. Whenever you give it a new string, it returns a seemingly random
number between 0 and 232 − 1. Even if the input strings are very similar, their
hashes are evenly distributed across that range of numbers. 
For partitioning purposes, the hash function need not be cryptographically strong: for example,
Cassandra and MongoDB use MD5, and Voldemort uses the Fowler–Noll–Vo function. Many programming
languages have simple hash functions built in (as they are used for hash tables), but they may not
be suitable for partitioning: for example, in Java’s Object.hashCode() and Ruby’s Object#hash,
the same key may have a different hash value in different processes
[[6](ch06.html#Kleppmann2012th)].