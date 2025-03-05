The locality advantage only applies if you need large parts of the document at the same time. The
database typically needs to load the entire document, even if you access only a small portion of it,
which can be wasteful on large documents. On updates to a document, the entire document usually
needs to be rewritten—only modifications that don’t change the encoded size of a document can
easily be performed in place [[19](ch02.html#Parikh2013vf)]. For these
reasons, it is generally recommended that you keep documents fairly small and avoid writes that
increase the size of a document [[9](ch02.html#MongoDB2013)]. These
performance limitations significantly reduce the set of situations in which document databases are
useful. 
It’s worth pointing out that the idea of grouping related data together for locality is not limited
to the document model. For example, Google’s Spanner database offers the same locality properties in
a relational data model, by allowing the schema to declare that a table’s rows should be interleaved
(nested) within a parent table
[[27](ch02.html#Corbett2012uz_ch2)].
Oracle allows the same, using a feature called multi-table index cluster tables
[[28](ch02.html#BurlesonCwtEpWL2)].
The column-family concept in the Bigtable data model (used in
Cassandra and HBase) has a similar purpose of managing locality
[[29](ch02.html#Chang2006ta_ch2)].