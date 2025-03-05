
When the underlying data changes, a materialized view needs to be updated, because it is a
denormalized copy of the data. The database can do that automatically, but such updates make writes
more expensive, which is why materialized views are not often used in OLTP databases. In read-heavy
data warehouses they can make more sense (whether or not they actually improve read performance
depends on the individual case). 
A common special case of a materialized view is known as a data cube or OLAP cube
[[64](ch03.html#Gray2007he)].
It is a grid of aggregates grouped by different dimensions. [Figure 3-12](#fig_data_cube) shows an example. ![ddia 0312](assets/ddia_0312.png) ###### Figure 3-12. Two dimensions of a data cube, aggregating data by summing. Imagine for now that each fact has foreign keys to only two dimension tables—in
[Figure 3-12](#fig_data_cube), these are date and product. You can now draw a two-dimensional table, with
dates along one axis and products along the other. Each cell contains the aggregate (e.g., SUM) of
an attribute (e.g., net_price) of all facts with that date-product combination. Then you can apply
the same aggregate along each row or column and get a summary that has been reduced by one
dimension (the sales by product regardless of date, or the sales by date regardless of product).