
Thus, Hadoop has often been used for implementing ETL processes (see [“Data Warehousing”](ch03.html#sec_storage_dwh)): data from
transaction processing systems is dumped into the distributed filesystem in some raw form, and then
MapReduce jobs are written to clean up that data, transform it into a relational form, and import it
into an MPP data warehouse for analytic purposes. Data modeling still happens, but it is in a
separate step, decoupled from the data collection. This decoupling is possible because a distributed
filesystem supports data encoded in any format. ### Diversity of processing models 
MPP databases are monolithic, tightly integrated pieces of software that take care of storage layout
on disk, query planning, scheduling, and execution. Since these components can all be tuned and
optimized for the specific needs of the database, the system as a whole can achieve very good
performance on the types of queries for which it is designed. Moreover, the SQL query language
allows expressive queries and elegant semantics without the need to write code, making it accessible
to graphical tools used by business analysts (such as Tableau).