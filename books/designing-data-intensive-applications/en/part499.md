
The approach of executing transactions serially is implemented in VoltDB/H-Store, Redis, and Datomic
[[46](ch07.html#Hugg2014ti),
[47](ch07.html#Kallman2008tf),
[48](ch07.html#Hickey2012wm)].
A system designed for single-threaded execution can sometimes perform better than a system that
supports concurrency, because it can avoid the coordination overhead of locking. However, its
throughput is limited to that of a single CPU core. In order to make the most of that single thread,
transactions need to be structured differently from their traditional form. ### Encapsulating transactions in stored procedures 
In the early days of databases, the intention was that a database transaction could encompass an
entire flow of user activity. For example, booking an airline ticket is a multi-stage process
(searching for routes, fares, and available seats; deciding on an itinerary; booking seats on
each of the flights of the itinerary; entering passenger details; making payment). Database
designers thought that it would be neat if that entire process was one transaction so that it could
be committed atomically.