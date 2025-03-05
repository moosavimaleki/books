### But what is the writer’s schema? 
There is an important question that we’ve glossed over so far: how does the reader know the writer’s
schema with which a particular piece of data was encoded? We can’t just include the entire schema
with every record, because the schema would likely be much bigger than the encoded data, making all
the space savings from the binary encoding futile. The answer depends on the context in which Avro is being used. To give a few examples: Large file with lots of records 
A common use for Avro—especially in the context of Hadoop—is for storing a large file
containing millions of records, all encoded with the same schema. (We will discuss this kind of
situation in [Chapter 10](ch10.html#ch_batch).) In this case, the writer of that file can just include the writer’s
schema once at the beginning of the file. Avro specifies a file format (object container files) to
do this.