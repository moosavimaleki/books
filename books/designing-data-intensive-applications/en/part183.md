
A compromise between a clustered index (storing all row data within the index) and a nonclustered
index (storing only references to the data within the index) is known as a covering index or
index with included columns, which stores some of a table’s columns within the index
[[33](ch03.html#Webb2008uj)].
This allows some queries to be answered by using the index alone (in which case, the index is said
to cover the query) [[32](ch03.html#SQLServer2012)]. As with any kind of duplication of data, clustered and covering indexes can speed up reads, but they
require additional storage and can add overhead on writes. Databases also need to go to additional
effort to enforce transactional guarantees, because applications should not see inconsistencies due
to the duplication. ### Multi-column indexes 
The indexes discussed so far only map a single key to a value. That is not sufficient if we need to
query multiple columns of a table (or multiple fields in a document) simultaneously.