
When a MapReduce job is given a set of files as input, it reads the entire content of all of those
files; a database would call this operation a full table scan. If you only want to read a small
number of records, a full table scan is outrageously expensive compared to an index lookup.
However, in analytic queries (see [“Transaction Processing or Analytics?”](ch03.html#sec_storage_analytics)) it is common to want to calculate
aggregates over a large number of records. In this case, scanning the entire input might be quite a
reasonable thing to do, especially if you can parallelize the processing across multiple machines. When we talk about joins in the context of batch processing, we mean resolving all occurrences of
some association within a dataset. For example, we assume that a job is processing the data for all
users simultaneously, not merely looking up the data for one particular user (which would be done
far more efficiently with an index).