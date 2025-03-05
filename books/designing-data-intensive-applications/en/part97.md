*  The structure of the data is determined by external systems over which you have no control and
which may change at any time. In situations like these, a schema may hurt more than it helps, and schemaless documents can be a
much more natural data model. But in cases where all records are expected to have the same
structure, schemas are a useful mechanism for documenting and enforcing that structure. We will
discuss schemas and schema evolution in more detail in [Chapter 4](ch04.html#ch_encoding). ### Data locality for queries 
A document is usually stored as a single continuous string, encoded as JSON, XML, or a binary variant
thereof (such as MongoDB’s BSON). If your application often needs to access the entire document
(for example, to render it on a web page), there is a performance advantage to this storage
locality. If data is split across multiple tables, like in [Figure 2-1](#fig_billgates_relational), multiple
index lookups are required to retrieve it all, which may require more disk seeks and take more time.