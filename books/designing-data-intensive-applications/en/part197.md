### The divergence between OLTP databases and data warehouses 
The data model of a data warehouse is most commonly relational, because SQL is generally a good fit
for analytic queries. There are many graphical data analysis tools that generate SQL queries,
visualize the results, and allow analysts to explore the data (through operations such as
drill-down and slicing and dicing). On the surface, a data warehouse and a relational OLTP database look similar, because they both have
a SQL query interface. However, the internals of the systems can look quite different, because they
are optimized for very different query patterns. Many database vendors now focus on supporting
either transaction processing or analytics workloads, but not both. 
Some databases, such as Microsoft SQL Server and SAP HANA, have support for transaction processing
and data warehousing in the same product. However, they are increasingly becoming two separate
storage and query engines, which happen to be accessible through a common SQL interface
[[49](ch03.html#Larson2013wh),
[50](ch03.html#Farber2012tw),
[51](ch03.html#OneSizeFitsNone2013vw)].