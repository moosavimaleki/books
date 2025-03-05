For these reasons, REST seems to be the predominant style for public APIs. The main focus of RPC
frameworks is on requests between services owned by the same organization, typically within the same
datacenter. ### Data encoding and evolution for RPC 
For evolvability, it is important that RPC clients and servers can be changed and deployed
independently. Compared to data flowing through databases (as described in the last section), we can make a
simplifying assumption in the case of dataflow through services: it is reasonable to assume that
all the servers will be updated first, and all the clients second. Thus, you only need backward
compatibility on requests, and forward compatibility on responses. The backward and forward compatibility properties of an RPC scheme are inherited from whatever
encoding it uses: *  Thrift, gRPC (Protocol Buffers), and Avro RPC can be evolved according to the compatibility rules
of the respective encoding format.