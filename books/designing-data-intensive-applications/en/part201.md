In a typical data warehouse, tables are often very wide: fact tables often have over 100 columns,
sometimes several hundred [[51](ch03.html#OneSizeFitsNone2013vw)].
Dimension tables can also be very wide, as they include all the metadata that may be relevant
for analysis—for example, the dim_store table may include details of which services are offered
at each store, whether it has an in-store bakery, the square footage, the date when the store was
first opened, when it was last remodeled, how far it is from the nearest highway, etc. # Column-Oriented Storage 
If you have trillions of rows and petabytes of data in your fact tables, storing and querying them
efficiently becomes a challenging problem. Dimension tables are usually much smaller (millions of
rows), so in this section we will concentrate primarily on storage of facts. Although fact tables are often over 100 columns wide, a typical data warehouse query only accesses 4
or 5 of them at one time ("SELECT *" queries are rarely needed for analytics)
[[51](ch03.html#OneSizeFitsNone2013vw)]. Take the query in
[Example 3-1](#fig_storage_analytics_query): it accesses a large number of rows (every occurrence of someone
buying fruit or candy during the 2013 calendar year), but it only needs to access three columns of
the fact_sales table: date_key, product_sk,
and quantity. The query ignores all other columns.