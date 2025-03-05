
The idea behind column-oriented storage is simple: don’t store all the values from one row
together, but store all the values from each column together instead. If each column is stored in
a separate file, a query only needs to read and parse those columns that are used in that query,
which can save a lot of work. This principle is illustrated in [Figure 3-10](#fig_column_store). ###### Note 
Column storage is easiest to understand in a relational data model, but it applies equally to
nonrelational data. For example, Parquet [[57](ch03.html#LeDem2013wc)] is a columnar storage format that supports a document
data model, based on Google’s Dremel [[54](ch03.html#Melnik2010up)]. ![ddia 0310](assets/ddia_0310.png) ###### Figure 3-10. Storing relational data by column, rather than by row. The column-oriented storage layout relies on each column file containing the rows in the same order.
Thus, if you need to reassemble an entire row, you can take the 23rd entry from each of the
individual column files and put them together to form the 23rd row of the table.