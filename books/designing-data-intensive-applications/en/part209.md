Another advantage of sorted order is that it can help with compression of columns. If the primary
sort column does not have many distinct values, then after sorting, it will have long sequences
where the same value is repeated many times in a row. A simple run-length encoding, like we used for
the bitmaps in [Figure 3-11](#fig_bitmap_index), could compress that column down to a few kilobytes—even if
the table has billions of rows. That compression effect is strongest on the first sort key. The second and third sort keys will be
more jumbled up, and thus not have such long runs of repeated values. Columns further down the
sorting priority appear in essentially random order, so they probably won’t compress as well. But
having the first few columns sorted is still a win overall. ### Several different sort orders 
A clever extension of this idea was introduced in C-Store and adopted in the commercial data
warehouse Vertica [[61](ch03.html#Stonebraker2005uf),
[62](ch03.html#Lamb2012ub)].
Different queries benefit from different sort orders, so why not store the same data sorted in
several different ways? Data needs to be replicated to multiple machines anyway, so that you don’t
lose data if one machine fails. You might as well store that redundant data sorted in different
ways so that when you’re processing a query, you can use the version that best fits the query
pattern.