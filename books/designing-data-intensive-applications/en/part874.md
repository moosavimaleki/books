## High-Level APIs and Languages 
Over the years since MapReduce first became popular, the execution engines for distributed batch
processing have matured. By now, the infrastructure has become robust enough to store and process
many petabytes of data on clusters of over 10,000 machines. As the problem of physically operating
batch processes at such scale has been considered more or less solved, attention has turned to other
areas: improving the programming model, improving the efficiency of processing, and broadening the
set of problems that these technologies can solve. 
As discussed previously, higher-level languages and APIs such as Hive, Pig, Cascading, and Crunch
became popular because programming MapReduce jobs by hand is quite laborious. As Tez emerged, these
high-level languages had the additional benefit of being able to move to the new dataflow execution
engine without the need to rewrite job code. Spark and Flink also include their own high-level
dataflow APIs, often taking inspiration from FlumeJava
[[34](ch10.html#Chambers2010dp)].