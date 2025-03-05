
In general, a “stream” refers to data that is incrementally made available over time. The concept
appears in many places: in the stdin and stdout of Unix, programming languages (lazy lists)
[[2](ch11.html#Abelson1996ut)],
filesystem APIs (such as Java’s FileInputStream), TCP connections, delivering audio and video over
the internet, and so on. In this chapter we will look at event streams as a data management mechanism: the unbounded,
incrementally processed counterpart to the batch data we saw in the
last chapter. We will first discuss how streams are
represented, stored, and transmitted over a network. In [“Databases and Streams”](#sec_stream_databases) we will investigate
the relationship between streams and databases. And
finally, in [“Processing Streams”](#sec_stream_processing) we will explore approaches and tools for processing those
streams continually, and ways that they can be used to
build applications. # Transmitting Event Streams In the batch processing world, the inputs and outputs of a job are files (perhaps on a distributed
filesystem). What does the streaming equivalent look like?