
Stream analytics systems sometimes use probabilistic algorithms, such as Bloom filters (which we
encountered in [“Performance optimizations”](ch03.html#sec_storage_lsm_optimize)) for set membership, HyperLogLog
[[72](ch11.html#Flajolet2007um)] for cardinality estimation, and various
percentile estimation algorithms (see [“Percentiles in Practice”](ch01.html#sidebar_percentiles)). Probabilistic algorithms produce
approximate results, but have the advantage of requiring significantly less memory in the stream
processor than exact algorithms. This use of approximation algorithms sometimes leads people to
believe that stream processing systems are always lossy and inexact, but that is wrong: there is
nothing inherently approximate about stream processing, and probabilistic algorithms are merely an
optimization [[73](ch11.html#Kreps2014wv_ch11)]. 
Many open source distributed stream processing frameworks are designed with analytics in mind: for
example, Apache Storm, Spark Streaming, Flink, Concord, Samza, and Kafka Streams
[[74](ch11.html#Hellstrom2016ub)].
Hosted services include Google Cloud Dataflow and Azure Stream Analytics. ### Maintaining materialized views 
We saw in [“Databases and Streams”](#sec_stream_databases) that a stream of changes to a database can be used to keep
derived data systems, such as caches, search indexes, and data warehouses, up to date with a source
database. We can regard these examples as specific cases of maintaining materialized views (see
[“Aggregation: Data Cubes and Materialized Views”](ch03.html#sec_storage_materialized_views)): deriving an alternative view onto some dataset so that you can
query it efficiently, and updating that view whenever the underlying data changes
[[50](ch11.html#Gupta1999uz)].