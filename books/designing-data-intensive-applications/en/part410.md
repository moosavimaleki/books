![ddia 0604](assets/ddia_0604.png) ###### Figure 6-4. Partitioning secondary indexes by document. In this indexing approach, each partition is completely separate: each partition maintains its own
secondary indexes, covering only the documents in that partition. It doesn’t care what data is
stored in other partitions. Whenever you need to write to the database—to add, remove, or update a
document—you only need to deal with the partition that contains the document ID that you are
writing. For that reason, a document-partitioned index is also known as a local index (as opposed
to a global index, described in the next section). However, reading from a document-partitioned index requires care: unless you have done something
special with the document IDs, there is no reason why all the cars with a particular color or a
particular make would be in the same partition. In [Figure 6-4](#fig_partitioning_secondary_by_doc), red cars
appear in both partition 0 and partition 1. Thus, if you want to search for red cars, you need to
send the query to all partitions, and combine all the results you get back.