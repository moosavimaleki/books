*  Like Unix tools, MapReduce jobs separate logic from wiring (configuring the input and output
directories), which provides a separation of concerns and enables potential reuse of code: one
team can focus on implementing a job that does one thing well, while other teams can decide where
and when to run that job. 
In these areas, the design principles that worked well for Unix also seem to be working well for
Hadoop—but Unix and Hadoop also differ in some ways. For example, because most Unix tools assume
untyped text files, they have to do a lot of input parsing (our log analysis example at the
beginning of the chapter used {print $7} to extract the URL).
 On Hadoop, some of those low-value syntactic conversions
are eliminated by using more structured file formats: Avro (see [“Avro”](ch04.html#sec_encoding_avro)) and Parquet
(see [“Column-Oriented Storage”](ch03.html#sec_storage_column)) are often used, as they provide efficient schema-based encoding and
allow evolution of their schemas over time (see [Chapter 4](ch04.html#ch_encoding)).