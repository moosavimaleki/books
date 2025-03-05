##### Example 3-1. Analyzing whether people are more inclined to buy fresh fruit or candy, depending on the day of the week ```
`SELECT`
  `dim_date``.``weekday``,` `dim_product``.``category``,`
  `SUM``(``fact_sales``.``quantity``)` `AS` `quantity_sold`
`FROM` `fact_sales`
  `JOIN` `dim_date`    `ON` `fact_sales``.``date_key`   `=` `dim_date``.``date_key`
  `JOIN` `dim_product` `ON` `fact_sales``.``product_sk` `=` `dim_product``.``product_sk`
`WHERE`
  `dim_date``.``year` `=` `2013` `AND`
  `dim_product``.``category` `IN` `(``'Fresh fruit'``,` `'Candy'``)`
`GROUP` `BY`
  `dim_date``.``weekday``,` `dim_product``.``category``;`
``` How can we execute this query efficiently? 
In most OLTP databases, storage is laid out in a row-oriented fashion: all the values from one row
of a table are stored next to each other. Document databases are similar: an entire document is
typically stored as one contiguous sequence of bytes. You can see this in the CSV example of
[Figure 3-1](#fig_storage_csv_hash_index). In order to process a query like [Example 3-1](#fig_storage_analytics_query), you may have indexes on
fact_sales.date_key and/or fact_sales.product_sk that tell the storage engine where to find
all the sales for a particular date or for a particular product. But then, a row-oriented storage
engine still needs to load all of those rows (each consisting of over 100 attributes) from disk into
memory, parse them, and filter out those that don’t meet the required conditions. That can take a
long time.