If n is very small (for example, a country column may have approximately 200 distinct values),
those bitmaps can be stored with one bit per row. But if n is bigger, there will be a lot of zeros
in most of the bitmaps (we say that they are sparse). In that case, the bitmaps can additionally
be run-length encoded, as shown at the bottom of [Figure 3-11](#fig_bitmap_index).  This can make the encoding
of a column remarkably compact. Bitmap indexes such as these are very well suited for the kinds of queries that are common in a data
warehouse. For example: `WHERE product_sk IN (30, 68, 69):` Load the three bitmaps for product_sk = 30, product_sk = 68, and product_sk = 69, and
calculate the bitwise OR of the three bitmaps, which can be done very efficiently. `WHERE product_sk = 31 AND store_sk = 3:` Load the bitmaps for product_sk = 31 and store_sk = 3, and calculate the bitwise AND. This
works because the columns contain the rows in the same order, so the kth bit in one column’s
bitmap corresponds to the same row as the kth bit in another column’s bitmap.