Backward compatibility 
Newer code can read data that was written by older code. Forward compatibility 
Older code can read data that was written by newer code. Backward compatibility is normally not hard to achieve: as author of the newer code, you know the
format of data written by older code, and so you can explicitly handle it (if necessary by simply
keeping the old code to read the old data). Forward compatibility can be trickier, because it
requires older code to ignore additions made by a newer version of the code. In this chapter we will look at several formats for encoding data, including JSON, XML, Protocol
Buffers, Thrift, and Avro. In particular, we will look at how they handle schema changes and how
they support systems where old and new data and code need to coexist. We will then discuss how those
formats are used for data storage and for communication: in web services, Representational State
Transfer (REST), and remote procedure calls (RPC), as well as message-passing systems such as actors
and message queues.