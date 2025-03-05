Having multiple sort orders in a column-oriented store is a bit similar to having multiple secondary
indexes in a row-oriented store. But the big difference is that the row-oriented store keeps every
row in one place (in the heap file or a clustered index), and secondary indexes just contain
pointers to the matching rows. In a column store, there normally aren’t any pointers to data
elsewhere, only columns containing values. ## Writing to Column-Oriented Storage 
These optimizations make sense in data warehouses, because most of the load consists of large
read-only queries run by analysts. Column-oriented storage, compression, and sorting all help to make
those read queries faster. However, they have the downside of making writes more difficult. An update-in-place approach, like B-trees use, is not possible with compressed columns. If you
wanted to insert a row in the middle of a sorted table, you would most likely have to rewrite all
the column files. As rows are identified by their position within a column, the insertion has to
update all columns consistently.