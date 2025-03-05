Note that it wouldn’t make sense to sort each column independently, because then we would no longer
know which items in the columns belong to the same row. We can only reconstruct a row because we
know that the kth item in one column belongs to the same row as the kth item in another
column. Rather, the data needs to be sorted an entire row at a time, even though it is stored by column.
The administrator of the database can choose the columns by which the table should be sorted, using
their knowledge of common queries. For example, if queries often target date ranges, such as the
last month, it might make sense to make date_key the first sort key. Then the query optimizer can
scan only the rows from the last month, which will be much faster than scanning all rows. A second column can determine the sort order of any rows that have the same value in the first
column. For example, if date_key is the first sort key in [Figure 3-10](#fig_column_store), it might make
sense for product_sk to be the second sort key so that all sales for the same product on the same
day are grouped together in storage. That will help queries that need to group or filter sales by
product within a certain date range.