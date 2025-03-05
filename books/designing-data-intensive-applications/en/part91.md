
However, when it comes to representing many-to-one and many-to-many relationships, relational and
document databases are not fundamentally different: in both cases, the related item is referenced by
a unique identifier, which is called a foreign key in the relational model and a document
reference in the document model [[9](ch02.html#MongoDB2013)]. That
identifier is resolved at read time by using a join or follow-up queries. To date, document
databases have not followed the path of CODASYL. ## Relational Versus Document Databases Today 
There are many differences to consider when comparing relational databases to document databases,
including their fault-tolerance properties (see [Chapter 5](ch05.html#ch_replication)) and handling of concurrency (see
[Chapter 7](ch07.html#ch_transactions)). In this chapter, we will concentrate only on the differences in the data model. The main arguments in favor of the document data model are schema flexibility, better performance
due to locality, and that for some applications it is closer to the data structures used by the
application. The relational model counters by providing better support for joins, and many-to-one
and many-to-many relationships.