For example, you can capture the changes in a database and continually apply the same changes to a
search index. If the log of changes is applied in the same order, you can expect the data in the
search index to match the data in the database. The search index and any other derived data systems
are just consumers of the change stream, as illustrated in [Figure 11-5](#fig_stream_change_capture). ![ddia 1105](assets/ddia_1105.png) ###### Figure 11-5. Taking data in the order it was written to one database, and applying the changes to other systems in the same order. ### Implementing change data capture 
We can call the log consumers derived data systems, as discussed in the introduction to
[Part III](part03.html#part_systems): the data stored in the search index and the data warehouse is just another view
onto the data in the system of record. Change data capture is a mechanism for ensuring that all
changes made to the system of record are also reflected in the derived data systems so that the
derived systems have an accurate copy of the data.