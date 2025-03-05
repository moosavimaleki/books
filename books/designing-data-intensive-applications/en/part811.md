
Each input file is typically hundreds of megabytes in size. The MapReduce scheduler (not shown in
the diagram) tries to run each mapper on one of the machines that stores a replica of the input
file, provided that machine has enough spare RAM and CPU resources to run the map task
[[26](ch10.html#White2015vl)].
This principle is known as putting the computation near the data
[[27](ch10.html#Gray2003vx)]: it saves copying the input file over the
network, reducing network load and increasing locality. ![ddia 1001](assets/ddia_1001.png) ###### Figure 10-1. A MapReduce job with three mappers and three reducers. In most cases, the application code that should run in the map task is not yet present on the
machine that is assigned the task of running it, so the MapReduce framework first copies the code
(e.g., JAR files in the case of a Java program) to the appropriate machines. It then starts the map
task and begins reading the input file, passing one record at a time to the mapper callback. The
output of the mapper consists of key-value pairs.