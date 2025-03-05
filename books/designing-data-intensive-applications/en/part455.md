But do we need multi-object transactions at all? Would it be possible to implement any application
with only a key-value data model and single-object operations? There are some use cases in which single-object inserts, updates, and deletes are sufficient.
However, in many other cases writes to several different objects need to be coordinated: *  
In a relational data model, a row in one table often has a foreign key reference to a row in
another table. (Similarly, in a graph-like data model, a vertex has edges to other vertices.)
Multi-object transactions allow you to ensure that these references remain valid: when inserting
several records that refer to one another, the foreign keys have to be correct and up to date,
or the data becomes nonsensical. *  
In a document data model, the fields that need to be updated together are often within the same
document, which is treated as a single object—no multi-object transactions are needed when
updating a single document. However, document databases lacking join functionality also encourage
denormalization (see [“Relational Versus Document Databases Today”](ch02.html#sec_datamodels_document_summary)). When denormalized information needs to
be updated, like in the example of [Figure 7-2](#fig_transactions_read_uncommitted), you need to update
several documents in one go. Transactions are very useful in this situation to prevent
denormalized data from going out of sync.