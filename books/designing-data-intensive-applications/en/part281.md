Message brokers typically don’t enforce any particular data model—a message is just a sequence of
bytes with some metadata, so you can use any encoding format. If the encoding is backward and
forward compatible, you have the greatest flexibility to change publishers and consumers
independently and deploy them in any order. If a consumer republishes messages to another topic, you may need to be careful to preserve unknown
fields, to prevent the issue described previously in the context of databases
([Figure 4-7](#fig_encoding_preserve_field)). ### Distributed actor frameworks 
The actor model is a programming model for concurrency in a single process. Rather than dealing
directly with threads (and the associated problems of race conditions, locking, and deadlock), logic
is encapsulated in actors. Each actor typically represents one client or entity, it may have some
local state (which is not shared with any other actor), and it communicates with other actors by
sending and receiving asynchronous messages. Message delivery is not guaranteed: in certain error
scenarios, messages will be lost. Since each actor processes only one message at a time, it doesn’t
need to worry about threads, and each actor can be scheduled independently by the framework.