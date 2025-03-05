On the other hand, MapReduce can tolerate the failure of a map or reduce task without it affecting the
job as a whole by retrying work at the granularity of an individual task. It is also very eager to
write data to disk, partly for fault tolerance, and partly on the assumption that the dataset will
be too big to fit in memory anyway. The MapReduce approach is more appropriate for larger jobs: jobs that process so much data and run
for such a long time that they are likely to experience at least one task failure along the way. In
that case, rerunning the entire job due to a single task failure would be wasteful. Even if
recovery at the granularity of an individual task introduces overheads that make fault-free
processing slower, it can still be a reasonable trade-off if the rate of task failures is high
enough. But how realistic are these assumptions? In most clusters, machine failures do occur, but they are
not very frequent—probably rare enough that most jobs will not experience a machine failure. Is
it really worth incurring significant overheads for the sake of fault tolerance?