## Message-Passing Dataflow 
We have been looking at the different ways encoded data flows from one process to another. So
far, we’ve discussed REST and RPC (where one process sends a request over the network to another
process and expects a response as quickly as possible), and databases (where one process writes
encoded data, and another process reads it again sometime in the future). In this final section, we will briefly look at asynchronous message-passing systems, which are
somewhere between RPC and databases. They are similar to RPC in that a client’s request (usually
called a message) is delivered to another process with low latency. They are similar to databases
in that the message is not sent via a direct network connection, but goes via an intermediary called
a message broker (also called a message queue or message-oriented middleware), which stores
the message temporarily. 
Using a message broker has several advantages compared to direct RPC: