Today, most data systems are not able to automatically compensate for such a highly skewed workload,
so it’s the responsibility of the application to reduce the skew. For example, if one key is known
to be very hot, a simple technique is to add a random number to the beginning or end of the key.
Just a two-digit decimal random number would split the writes to the key evenly across 100 different
keys, allowing those keys to be distributed to different partitions. However, having split the writes across different keys, any reads now have to do additional work, as
they have to read the data from all 100 keys and combine it. This technique also requires additional
bookkeeping: it only makes sense to append the random number for the small number of hot keys; for
the vast majority of keys with low write throughput this would be unnecessary overhead. Thus, you
also need some way of keeping track of which keys are being split.