
A batch job’s output is only considered valid when the job has completed successfully (MapReduce
discards the partial output of a failed job). Therefore, one job in a workflow can only start when
the prior jobs—that is, the jobs that produce its input directories—have completed
successfully. To handle these dependencies between job executions, various workflow schedulers for
Hadoop have been developed, including Oozie, Azkaban, Luigi, Airflow, and Pinball
[[28](ch10.html#Trencseni2016vn)]. 
These schedulers also have management features that are useful when maintaining a large collection
of batch jobs. Workflows consisting of 50 to 100 MapReduce jobs are common when building
recommendation systems
[[29](ch10.html#Sumbaly2013eh)],
and in a large organization, many different teams may be running different jobs that read each
other’s output. Tool support is important for managing such complex dataflows. 
Various higher-level tools for Hadoop, such as Pig
[[30](ch10.html#Gates2009vg)], Hive
[[31](ch10.html#Thusoo2010hp)],
Cascading
[[32](ch10.html#CascadingDocs)], Crunch
[[33](ch10.html#ApacheCrunch)], and FlumeJava
[[34](ch10.html#Chambers2010dp)],
also set up workflows of multiple MapReduce stages that are automatically wired together
appropriately.