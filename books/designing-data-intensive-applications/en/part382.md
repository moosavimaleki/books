### Version vectors 
The example in [Figure 5-13](#fig_replication_causality_single) used only a single replica. How does the
algorithm change when there are multiple replicas, but no leader? [Figure 5-13](#fig_replication_causality_single) uses a single version number to capture dependencies between
operations, but that is not sufficient when there are multiple replicas accepting writes
concurrently. Instead, we need to use a version number per replica as well as per key. Each
replica increments its own version number when processing a write, and also keeps track of the
version numbers it has seen from each of the other replicas. This information indicates which values
to overwrite and which values to keep as siblings. 
The collection of version numbers from all the replicas is called a version vector
[[56](ch05.html#ParkerJr1983jb)].
A few variants of this idea are in use, but the most interesting is probably the dotted version
vector
[[57](ch05.html#Preguica2010wu)], which is used in Riak 2.0
[[58](ch05.html#Cribbs2014wc), [59](ch05.html#Brown2015wx)].
We won’t go into the details, but the way it works is quite similar to what we saw in our cart example.