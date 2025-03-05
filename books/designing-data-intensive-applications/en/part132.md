No. They differ in several important ways: *  In CODASYL, a database had a schema that specified which record type could be nested within which
other record type. In a graph database, there is no such restriction: any vertex can have an edge
to any other vertex. This gives much greater flexibility for applications to adapt to changing
requirements. *  
In CODASYL, the only way to reach a particular record was to traverse one of the access paths to
it. In a graph database, you can refer directly to any vertex by its unique ID, or you can use an
index to find vertices with a particular value. *  In CODASYL, the children of a record were an ordered set, so the database had to maintain that
ordering (which had consequences for the storage layout) and applications that inserted new
records into the database had to worry about the positions of the new records in these sets. In a
graph database, vertices and edges are not ordered (you can only sort the results when making a
query).