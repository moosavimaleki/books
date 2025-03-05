We then took a detour from the internals of storage engines to look at the high-level architecture
of a typical data warehouse. This background illustrated why analytic workloads are so different
from OLTP: when your queries require sequentially scanning across a large number of rows, indexes
are much less relevant. Instead it becomes important to encode data very compactly, to minimize the
amount of data that the query needs to read from disk. We discussed how column-oriented storage
helps achieve this goal. As an application developer, if you’re armed with this knowledge about the internals of storage
engines, you are in a much better position to know which tool is best suited for your particular
application. If you need to adjust a database’s tuning parameters, this understanding allows you to
imagine what effect a higher or a lower value may have. Although this chapter couldn’t make you an expert in tuning any one particular storage engine, it
has hopefully equipped you with enough vocabulary and ideas that you can make sense of the
documentation for the database of your choice.