## Column Compression 
Besides only loading those columns from disk that are required for a query, we can further reduce
the demands on disk throughput by compressing data. Fortunately, column-oriented storage often lends
itself very well to compression. 
Take a look at the sequences of values for each column in [Figure 3-10](#fig_column_store): they often look quite
repetitive, which is a good sign for compression. Depending on the data in the column, different
compression techniques can be used. One technique that is particularly effective in data warehouses
is bitmap encoding, illustrated in [Figure 3-11](#fig_bitmap_index). ![ddia 0311](assets/ddia_0311.png) ###### Figure 3-11. Compressed, bitmap-indexed storage of a single column. Often, the number of distinct values in a column is small compared to the number of rows (for
example, a retailer may have billions of sales transactions, but only 100,000 distinct products).
We can now take a column with n distinct values and turn it into n separate bitmaps: one bitmap
for each distinct value, with one bit for each row. The bit is 1 if the row has that value, and 0 if
not.