# Summary In this chapter we tried to get to the bottom of how databases handle storage and retrieval. What
happens when you store data in a database, and what does the database do when you query for the
data again later? On a high level, we saw that storage engines fall into two broad categories: those optimized for
transaction processing (OLTP), and those optimized for analytics (OLAP). There are big differences between
the access patterns in those use cases: *  OLTP systems are typically user-facing, which means that they may see a huge volume of requests.
In order to handle the load, applications usually only touch a small number of records in each
query. The application requests records using some kind of key, and the storage engine uses an
index to find the data for the requested key. Disk seek time is often the bottleneck here. *  Data warehouses and similar analytic systems are less well known, because they are primarily used
by business analysts, not by end users. They handle a much lower volume of queries than OLTP
systems, but each query is typically very demanding, requiring many millions of records to be
scanned in a short time. Disk bandwidth (not seek time) is often the bottleneck here, and
column-oriented storage is an increasingly popular solution for this kind of workload.