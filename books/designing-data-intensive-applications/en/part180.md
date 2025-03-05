B-trees are very ingrained in the architecture of databases and provide consistently good
performance for many workloads, so it’s unlikely that they will go away anytime soon. In new
datastores, log-structured indexes are becoming increasingly popular. There is no quick and easy
rule for determining which type of storage engine is better for your use case, so it is worth
testing empirically. ## Other Indexing Structures 
So far we have only discussed key-value indexes, which are like a primary key index in the
relational model. A primary key uniquely identifies one row in a relational table, or one document
in a document database, or one vertex in a graph database. Other records in the database can refer
to that row/document/vertex by its primary key (or ID), and the index is used to resolve such
references. 
It is also very common to have secondary indexes. In relational databases, you can create several
secondary indexes on the same table using the CREATE INDEX command, and they are often crucial
for performing joins efficiently. For example, in [Figure 2-1](ch02.html#fig_billgates_relational) in [Chapter 2](ch02.html#ch_datamodels)
you would most likely have a secondary index on the user_id columns so that you can find all the
rows belonging to the same user in each of the tables.