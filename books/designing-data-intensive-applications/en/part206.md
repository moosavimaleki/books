There are also various other compression schemes for different kinds of data, but we won’t go into
them in detail—see
[[58](ch03.html#Abadi2013kf)]
for an overview. # Column-oriented storage and column families 
Cassandra and HBase have a concept of column families, which they inherited from Bigtable
[[9](ch03.html#Chang2006ta_ch3)]. However, it is very misleading to
call them column-oriented: within each column family, they store all columns from a row together,
along with a row key, and they do not use column compression. Thus, the Bigtable model is still
mostly row-oriented. ### Memory bandwidth and vectorized processing 
For data warehouse queries that need to scan over millions of rows, a big bottleneck is the
bandwidth for getting data from disk into memory. However, that is not the only bottleneck.
Developers of analytical databases also worry about efficiently using the bandwidth from
main memory into the CPU cache, avoiding branch mispredictions and bubbles in the CPU instruction
processing pipeline, and making use of single-instruction-multi-data (SIMD) instructions in modern
CPUs [[59](ch03.html#Boncz2005ws),
[60](ch03.html#Zhou2002gu)].