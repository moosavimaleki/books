# Chapter 11. Stream Processing

# Chapter 11. Stream Processing A complex system that works is invariably found to have evolved from a simple system that works.
The inverse proposition also appears to be true: A complex system designed from scratch never works
and cannot be made to work. John Gall, Systemantics (1975) ![](assets/ch11-map-ebook.png) 
In [Chapter 10](ch10.html#ch_batch) we discussed batch processing—techniques that read a set of files as input and
produce a new set of output files. The output is a form of derived data; that is, a dataset that
can be recreated by running the batch process again if necessary. We saw how this simple but
powerful idea can be used to create search indexes, recommendation systems, analytics, and more. 
However, one big assumption remained throughout [Chapter 10](ch10.html#ch_batch): namely, that the input is bounded—i.e., of a
known and finite size—so the batch process knows when it has finished reading its input. For
example, the sorting operation that is central to MapReduce must read its entire input before it can
start producing output: it could happen that the very last input record is the one with the lowest
key, and thus needs to be the very first output record, so starting the output early is not an
option.