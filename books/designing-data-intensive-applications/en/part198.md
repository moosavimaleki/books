
Data warehouse vendors such as Teradata, Vertica, SAP HANA, and ParAccel typically sell their systems
under expensive commercial licenses. Amazon RedShift is a hosted version of ParAccel. More recently,
a plethora of open source SQL-on-Hadoop projects have emerged; they are young but aiming to compete
with commercial data warehouse systems. These include Apache Hive, Spark SQL, Cloudera Impala,
Facebook Presto, Apache Tajo, and Apache Drill [[52](ch03.html#Abadi2013vf),
[53](ch03.html#Kornacker2015uv_ch3)].
Some of them are based on ideas from Google’s Dremel
[[54](ch03.html#Melnik2010up)]. ## Stars and Snowflakes: Schemas for Analytics 
As explored in [Chapter 2](ch02.html#ch_datamodels), a wide range of different data models are used in the realm of
transaction processing, depending on the needs of the application. On the other hand, in analytics,
there is much less diversity of data models. Many data warehouses are used in a fairly formulaic
style, known as a star schema (also known as dimensional modeling
[[55](ch03.html#Kimball2013tb_ch3)]). 
The example schema in [Figure 3-9](#fig_dwh_schema) shows a data warehouse that might be found at a grocery
retailer. At the center of the schema is a so-called fact table (in this example, it is called
fact_sales). Each row of the fact table represents an event that occurred at a particular time
(here, each row represents a customer’s purchase of a product). If we were analyzing website traffic
rather than retail sales, each row might represent a page view or a click by a user.