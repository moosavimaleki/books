### The move toward declarative query languages 
An advantage of specifying joins as relational operators, compared to spelling out the code that
performs the join, is that the framework can analyze the properties of the join inputs and
automatically decide which of the aforementioned join algorithms would be most suitable for the task
at hand. Hive, Spark, and Flink have cost-based query optimizers that can do this, and even change
the order of joins so that the amount of intermediate state is minimized
[[66](ch10.html#Alexandrov2014jb),
[77](ch10.html#Huske2015vm),
[78](ch10.html#Mokhtar2015vg),
[79](ch10.html#Armbrust2015dy)]. 
The choice of join algorithm can make a big difference to the performance of a batch job, and it is
nice not to have to understand and remember all the various join algorithms we discussed in this
chapter. This is possible if joins are specified in a declarative way: the application simply
states which joins are required, and the query optimizer decides how they can best be executed.
We previously came across this idea in [“Query Languages for Data”](ch02.html#sec_datamodels_query).