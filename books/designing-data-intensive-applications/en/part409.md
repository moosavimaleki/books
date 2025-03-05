The problem with secondary indexes is that they don’t map neatly to partitions. There are two main
approaches to partitioning a database with secondary indexes: document-based partitioning
and term-based partitioning. ## Partitioning Secondary Indexes by Document 
For example, imagine you are operating a website for selling used cars (illustrated in
[Figure 6-4](#fig_partitioning_secondary_by_doc)). Each listing has a unique ID—call it the document ID—and
you partition the database by the document ID (for example, IDs 0 to 499 in partition 0, IDs 500 to 999
in partition 1, etc.). You want to let users search for cars, allowing them to filter by color and by make, so you need
a secondary index on color and make (in a document database these would be fields; in a
relational database they would be columns). If you have declared the index, the database can perform
the indexing automatically.[ii](ch06.html#idm140605775218496)
For example, whenever a red car is added to the database, the database partition automatically adds
it to the list of document IDs for the index entry color:red.