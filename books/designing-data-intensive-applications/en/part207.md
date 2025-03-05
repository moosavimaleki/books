
Besides reducing the volume of data that needs to be loaded from disk, column-oriented storage
layouts are also good for making efficient use of CPU cycles. For example, the query engine can take
a chunk of compressed column data that fits comfortably in the CPU’s L1 cache and iterate through
it in a tight loop (that is, with no function calls). A CPU can execute such a loop much faster than code
that requires a lot of function calls and conditions for each record that is processed. Column
compression allows more rows from a column to fit in the same amount of L1 cache. Operators, such as
the bitwise AND and OR described previously, can be designed to operate on such chunks of
compressed column data directly. This technique is known as vectorized processing
[[58](ch03.html#Abadi2013kf),
[49](ch03.html#Larson2013wh)]. ## Sort Order in Column Storage 
In a column store, it doesn’t necessarily matter in which order the rows are stored. It’s easiest to
store them in the order in which they were inserted, since then inserting a new row just means
appending to each of the column files. However, we can choose to impose an order, like we did with
SSTables previously, and use that as an indexing mechanism.