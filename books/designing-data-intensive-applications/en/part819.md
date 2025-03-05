
The simplest implementation of this join would go over the activity events one by one and query the
user database (on a remote server) for every user ID it encounters. This is possible, but it would
most likely suffer from very poor performance: the processing throughput would be limited by the
round-trip time to the database server, the effectiveness of a local cache would depend very much on
the distribution of data, and running a large number of queries in parallel could easily overwhelm
the database [[35](ch10.html#Kreps2014wm_ch10)]. 
In order to achieve good throughput in a batch process, the computation must be (as much as
possible) local to one machine. Making random-access requests over the network for every record you
want to process is too slow. Moreover, querying a remote database would mean that the batch job
becomes nondeterministic, because the data in the remote database might change. 
Thus, a better approach would be to take a copy of the user database (for example, extracted from a
database backup using an ETL process—see [“Data Warehousing”](ch03.html#sec_storage_dwh)) and to put it in the same distributed
filesystem as the log of user activity events. You would then have the user database in one set of
files in HDFS and the user activity records in another set of files, and could use MapReduce to
bring together all of the relevant records in the same place and process them efficiently.