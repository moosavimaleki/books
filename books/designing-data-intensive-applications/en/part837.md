Alternatively, it is possible to build indexes incrementally. As discussed in [Chapter 3](ch03.html#ch_storage), if you
want to add, remove, or update documents in an index, Lucene writes out new segment
files and asynchronously merges and compacts segment files in the background. We will see more
on such incremental processing in [Chapter 11](ch11.html#ch_stream). ### Key-value stores as batch process output 
Search indexes are just one example of the possible outputs of a batch processing workflow. Another
common use for batch processing is to build machine learning systems such as classifiers (e.g., spam
filters, anomaly detection, image recognition) and recommendation systems (e.g., people you may know,
products you may be interested in, or related searches
[[29](ch10.html#Sumbaly2013eh)]). 
The output of those batch jobs is often some kind of database: for example, a database that can be
queried by user ID to obtain suggested friends for that user, or a database that can be queried by
product ID to get a list of related products
[[45](ch10.html#Wu2014tm)].