
If you need to perform a full-text search over a fixed set of documents, then a batch process is a
very effective way of building the indexes: the mappers partition the set of documents as needed,
each reducer builds the index for its partition, and the index files are written to the distributed
filesystem. Building such document-partitioned indexes (see [“Partitioning and Secondary Indexes”](ch06.html#sec_partitioning_secondary_indexes))
parallelizes very well. Since querying a search index by keyword is a read-only operation, these
index files are immutable once they have been created. If the indexed set of documents changes, one option is to periodically rerun the entire indexing
workflow for the entire set of documents, and replace the previous index files wholesale with the
new index files when it is done. This approach can be computationally expensive if only a small number of
documents have changed, but it has the advantage that the indexing process is very easy to reason
about: documents in, indexes out.