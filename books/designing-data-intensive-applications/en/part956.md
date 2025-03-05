The one crucial difference to batch jobs is that a stream never ends. This difference has many
implications: as discussed at the start of this chapter, sorting does not make sense with an
unbounded dataset, and so sort-merge joins (see [“Reduce-Side Joins and Grouping”](ch10.html#sec_batch_reduce_joins)) cannot be used.
Fault-tolerance mechanisms must also change: with a batch job that has been running for a few
minutes, a failed task can simply be restarted from the beginning, but with a stream job that has
been running for several years, restarting from the beginning after a crash may not be a viable option. ## Uses of Stream Processing Stream processing has long been used for monitoring purposes, where an organization wants to be
alerted if certain things happen. For example: *  Fraud detection systems need to determine if the usage patterns of a credit card have unexpectedly
changed, and block the card if it is likely to have been stolen.