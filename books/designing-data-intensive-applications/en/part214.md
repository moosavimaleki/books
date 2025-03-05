In general, facts often have more than two dimensions. In [Figure 3-9](#fig_dwh_schema) there are five
dimensions: date, product, store, promotion, and customer. It’s a lot harder to imagine what a
five-dimensional hypercube would look like, but the principle remains the same: each cell contains
the sales for a particular date-product-store-promotion-customer combination. These values can then
repeatedly be summarized along each of the dimensions. The advantage of a materialized data cube is that certain queries become very fast because they
have effectively been precomputed. For example, if you want to know the total sales per store
yesterday, you just need to look at the totals along the appropriate dimension—no need to scan
millions of rows. The disadvantage is that a data cube doesn’t have the same flexibility as querying the raw data. For example,
there is no way of calculating which proportion of sales comes from items that cost more than $100,
because the price isn’t one of the dimensions. Most data warehouses therefore try to keep as much
raw data as possible, and use aggregates such as data cubes only as a performance boost for certain
queries.