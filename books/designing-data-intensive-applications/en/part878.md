
However, dataflow engines have found that there are also advantages to incorporating more
declarative features in areas besides joins. For example, if a callback function contains only a
simple filtering condition, or it just selects some fields from a record, then there is significant
CPU overhead in calling the function on every record. If such simple filtering and mapping
operations are expressed in a declarative way, the query optimizer can take advantage of
column-oriented storage layouts (see [“Column-Oriented Storage”](ch03.html#sec_storage_column)) and read only the required columns from
disk. Hive, Spark DataFrames, and Impala also use vectorized execution (see
[“Memory bandwidth and vectorized processing”](ch03.html#sec_storage_vectorized)): iterating over data in a tight inner loop that is friendly to CPU
caches, and avoiding function calls. Spark generates JVM bytecode
[[79](ch10.html#Armbrust2015dy)] and Impala uses LLVM to generate native
code for these inner loops [[41](ch10.html#Kornacker2015uv_ch10)]. By incorporating declarative aspects in their high-level APIs, and having query optimizers that can
take advantage of them during execution, batch processing frameworks begin to look more like MPP
databases (and can achieve comparable performance). At the same time, by having the extensibility of
being able to run arbitrary code and read data in arbitrary formats, they retain their flexibility
advantage.