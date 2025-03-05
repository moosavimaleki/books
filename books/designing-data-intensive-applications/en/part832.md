If a map-side merge join is possible, it probably means that prior MapReduce jobs brought the input
datasets into this partitioned and sorted form in the first place. In principle, this join could
have been performed in the reduce stage of the prior job. However, it may still be appropriate to
perform the merge join in a separate map-only job, for example if the partitioned and sorted
datasets are also needed for other purposes besides this particular join. ### MapReduce workflows with map-side joins 
When the output of a MapReduce join is consumed by downstream jobs, the choice of map-side or
reduce-side join affects the structure of the output. The output of a reduce-side join is
partitioned and sorted by the join key, whereas the output of a map-side join is partitioned and
sorted in the same way as the large input (since one map task is started for each file block of the
join’s large input, regardless of whether a partitioned or broadcast join is used).