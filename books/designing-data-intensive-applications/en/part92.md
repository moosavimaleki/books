### Which data model leads to simpler application code? 
If the data in your application has a document-like structure (i.e., a tree of one-to-many
relationships, where typically the entire tree is loaded at once), then it’s probably a good idea to
use a document model. The relational technique of shredding—splitting a document-like structure
into multiple tables (like positions, education, and contact_info in
[Figure 2-1](#fig_billgates_relational))—can lead to cumbersome schemas and unnecessarily complicated
application code. The document model has limitations: for example, you cannot refer directly to a nested item
within a document, but instead you need to say something like “the second item in the list of
positions for user 251” (much like an access path in the hierarchical model). However, as long as
documents are not too deeply nested, that is not usually a problem. 
The poor support for joins in document databases may or may not be a problem, depending on the
application. For example, many-to-many relationships may never be needed in an analytics application
that uses a document database to record which events occurred at which time
[[19](ch02.html#Parikh2013vf)].