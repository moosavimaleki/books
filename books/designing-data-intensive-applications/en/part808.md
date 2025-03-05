4.  Call the reducer function to iterate over the sorted key-value pairs. If there are multiple
occurrences of the same key, the sorting has made them adjacent in the list, so it is easy to
combine those values without having to keep a lot of state in memory. In the preceding example,
the reducer is implemented by the command uniq -c, which counts the number of adjacent records
with the same key. Those four steps can be performed by one MapReduce job. Steps 2 (map) and 4 (reduce) are where you
write your custom data processing code. Step 1 (breaking files into records) is handled by the input
format parser. Step 3, the sort step, is implicit in MapReduce—you don’t have to write it, because the
output from the mapper is always sorted before it is given to the reducer. 
To create a MapReduce job, you need to implement two callback functions, the mapper and reducer, which
behave as follows (see also [“MapReduce Querying”](ch02.html#sec_datamodels_mapreduce)):