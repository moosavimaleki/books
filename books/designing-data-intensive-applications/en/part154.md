![ddia 0301](assets/ddia_0301.png) ###### Figure 3-1. Storing a log of key-value pairs in a CSV-like format, indexed with an in-memory hash map. 
This may sound simplistic, but it is a viable approach. In fact, this is essentially what Bitcask
(the default storage engine in Riak) does
[[3](ch03.html#Sheehy2010uy)].
Bitcask offers high-performance reads and writes, subject to the requirement that all the keys fit
in the available RAM, since the hash map is kept completely in memory. The values can use more space
than there is available memory, since they can be loaded from disk with just one disk seek. If that part of
the data file is already in the filesystem cache, a read doesn’t require any disk I/O at all. A storage engine like Bitcask is well suited to situations where the value for each key is updated
frequently. For example, the key might be the URL of a cat video, and the value might be the number
of times it has been played (incremented every time someone hits the play button). In this kind of
workload, there are a lot of writes, but there are not too many distinct keys—you have a large
number of writes per key, but it’s feasible to keep all keys in memory.