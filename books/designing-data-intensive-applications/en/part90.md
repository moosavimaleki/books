If you want to query your data in new ways, you can just declare a new index, and queries will
automatically use whichever indexes are most appropriate. You don’t need to change your queries to
take advantage of a new index. (See also [“Query Languages for Data”](#sec_datamodels_query).) The relational model thus made
it much easier to add new features to applications. Query optimizers for relational databases are complicated beasts, and they have consumed many years
of research and development effort
[[18](ch02.html#Hellerstein2007be)].
But a key insight of the relational model was this: you only need to build a query optimizer once,
and then all applications that use the database can benefit from it. If you don’t have a query
optimizer, it’s easier to handcode the access paths for a particular query than to write a
general-purpose optimizer—but the general-purpose solution wins in the long run. ### Comparison to document databases Document databases reverted back to the hierarchical model in one aspect: storing nested records
(one-to-many relationships, like positions, education, and contact_info in
[Figure 2-1](#fig_billgates_relational)) within their parent record rather than in a separate table.