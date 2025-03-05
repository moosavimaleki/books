
Therefore, according to this definition, there are no concurrent operations in a linearizable
datastore: there must be a single timeline along which all operations are totally ordered. There
might be several requests waiting to be handled, but the datastore ensures that every request is
handled atomically at a single point in time, acting on a single copy of the data, along a single
timeline, without any concurrency. Concurrency would mean that the timeline branches and merges again—and in this case, operations on
different branches are incomparable (i.e., concurrent). We saw this phenomenon in
[Chapter 5](ch05.html#ch_replication): for example, [Figure 5-14](ch05.html#fig_replication_causal_dependencies) is not a straight-line
total order, but rather a jumble of different operations going on concurrently. The arrows in the
diagram indicate causal dependencies—the partial ordering of operations. 
If you are familiar with distributed version control systems such as Git, their version histories
are very much like the graph of causal dependencies. Often one commit happens after another, in a
straight line, but sometimes you get branches (when several people concurrently work on a project),
and merges are created when those concurrently created commits are combined.