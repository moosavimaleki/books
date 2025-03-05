### Making an LSM-tree out of SSTables 
The algorithm described here is essentially what is used in LevelDB
[[6](ch03.html#LevelDB2014)] and RocksDB
[[7](ch03.html#Borthakur2013uc)], key-value storage engine
libraries that are designed to be embedded into other applications.
Among other things, LevelDB can be used in Riak as an alternative to Bitcask.
Similar storage engines are used in Cassandra and HBase
[[8](ch03.html#Bertozzi2012wu)], both of which were inspired by
Google’s Bigtable paper
[[9](ch03.html#Chang2006ta_ch3)] (which introduced the terms SSTable and
memtable). Originally this indexing structure was described by Patrick O’Neil et al. under the name
Log-Structured Merge-Tree (or LSM-Tree) [[10](ch03.html#ONeil1996iq)],
building on earlier work on log-structured filesystems
[[11](ch03.html#Rosenblum1992dr)].
Storage engines that are based on this principle of merging and compacting sorted files are often
called LSM storage engines. 
Lucene, an indexing engine for full-text search used by Elasticsearch and Solr, uses a similar
method for storing its term dictionary
[[12](ch03.html#Grand2013ws),
[13](ch03.html#Kandepet2011uy)].
A full-text index is much more complex than a key-value index but is based on a similar idea:
given a word in a search query, find all the documents (web pages, product descriptions, etc.) that
mention the word. This is implemented with a key-value structure where the key is a word (a term)
and the value is the list of IDs of all the documents that contain the word (the postings list).
In Lucene, this mapping from term to postings list is kept in SSTable-like sorted files, which are
merged in the background as needed
[[14](ch03.html#McCandless2011vt)].