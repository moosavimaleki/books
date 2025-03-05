These OLTP systems are usually expected to be highly available and to process transactions with low
latency, since they are often critical to the operation of the business. Database administrators
therefore closely guard their OLTP databases. They are usually reluctant to let business analysts
run ad hoc analytic queries on an OLTP database, since those queries are often expensive, scanning
large parts of the dataset, which can harm the performance of concurrently executing transactions. 
A data warehouse, by contrast, is a separate database that analysts can query to their hearts’
content, without affecting OLTP operations
[[48](ch03.html#Chaudhuri1997bd)].
The data warehouse contains a read-only copy of the data in all the various OLTP systems in the
company. Data is extracted from OLTP databases (using either a periodic data dump or a continuous
stream of updates), transformed into an analysis-friendly schema, cleaned up, and then loaded into
the data warehouse. This process of getting data into the warehouse is known as
Extract–Transform–Load (ETL) and is illustrated in [Figure 3-8](#fig_dwh_etl).