Perhaps in the future, data systems will be able to automatically detect and compensate for skewed
workloads; but for now, you need to think through the trade-offs for your own application. # Partitioning and Secondary Indexes 
The partitioning schemes we have discussed so far rely on a key-value data model. If records are
only ever accessed via their primary key, we can determine the partition from that key and use it
to route read and write requests to the partition responsible for that key. The situation becomes more complicated if secondary indexes are involved (see also
[“Other Indexing Structures”](ch03.html#sec_storage_other_indexing)). A secondary index usually doesn’t identify a record uniquely but
rather is a way of searching for occurrences of a particular value: find all actions by user
123, find all articles containing the word hogwash, find all cars whose color is red, and so
on. 
Secondary indexes are the bread and butter of relational databases, and they are common in document
databases too. Many key-value stores (such as HBase and Voldemort) have avoided secondary indexes
because of their added implementation complexity, but some (such as Riak) have started adding them
because they are so useful for data modeling. And finally, secondary indexes are the raison d’être
of search servers such as Solr and Elasticsearch.