###### Note 
Dataflow engines like Spark, Flink, and Tez (see [“Materialization of Intermediate State”](#sec_batch_materialize)) typically arrange the
operators in a job as a directed acyclic graph (DAG). This is not the same as graph processing: in
dataflow engines, the flow of data from one operator to another is structured as a graph, while
the data itself typically consists of relational-style tuples. In graph processing, the data
itself has the form of a graph. Another unfortunate naming confusion! 
Many graph algorithms are expressed by traversing one edge at a time, joining one vertex with an
adjacent vertex in order to propagate some information, and repeating until some condition is
met—for example, until there are no more edges to follow, or until some metric converges. We saw an
example in [Figure 2-6](ch02.html#fig_datalog_naive), which made a list of all the locations in North America contained
in a database by repeatedly following edges indicating which location is within which other location
(this kind of algorithm is called a transitive closure).