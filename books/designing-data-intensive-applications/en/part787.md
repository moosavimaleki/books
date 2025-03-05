Stream processing systems (near-real-time systems) 
Stream processing is somewhere between online and offline/batch processing (so it is sometimes
called near-real-time or nearline processing). Like a batch processing system, a stream
processor consumes inputs and produces outputs (rather than responding to requests). However, a
stream job operates on events shortly after they happen, whereas a batch job operates on a fixed
set of input data.  This difference allows stream processing systems to have lower latency than
the equivalent batch systems. As stream processing builds upon batch processing, we discuss it in
[Chapter 11](ch11.html#ch_stream). 
As we shall see in this chapter, batch processing is an important building block in our quest to
build reliable, scalable, and maintainable applications. For example, MapReduce, a batch processing
algorithm published in 2004
[[1](ch10.html#Dean2004ua_ch10)], was (perhaps
over-enthusiastically) called “the algorithm that makes Google so massively scalable”
[[2](ch10.html#Spolsky2005wm)]. It was subsequently
implemented in various open source data systems, including Hadoop, CouchDB, and MongoDB.