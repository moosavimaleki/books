Mapper The mapper is called once for every input record, and its job is to extract the key and
value from the input record. For each input, it may generate any number of key-value pairs
(including none). It does not keep any state from one input record to the next, so each record is
handled independently. Reducer The MapReduce framework takes the key-value pairs produced by the mappers, collects all the values
belonging to the same key, and calls the reducer with an iterator over that collection of
values. The reducer can produce output records (such as the number of occurrences of the same
URL). In the web server log example, we had a second sort command in step 5, which ranked URLs by number
of requests. In MapReduce, if you need a second sorting stage, you can implement it by writing a
second MapReduce job and using the output of the first job as input to the second job. Viewed like
this, the role of the mapper is to prepare the data by putting it into a form that is suitable for
sorting, and the role of the reducer is to process the data that has been sorted.