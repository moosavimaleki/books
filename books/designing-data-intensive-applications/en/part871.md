
It’s a bit similar to the actor model (see [“Distributed actor frameworks”](ch04.html#sec_encoding_actors)), if you think of each vertex as
an actor, except that vertex state and messages between vertices are fault-tolerant and durable, and
communication proceeds in fixed rounds: at every iteration, the framework delivers all messages sent
in the previous iteration. Actors normally have no such timing guarantee. ### Fault tolerance 
The fact that vertices can only communicate by message passing (not by querying each other directly)
helps improve the performance of Pregel jobs, since messages can be batched and there is less
waiting for communication. The only waiting is between iterations: since the Pregel model guarantees
that all messages sent in one iteration are delivered in the next iteration, the prior iteration
must completely finish, and all of its messages must be copied over the network, before the next one
can start. Even though the underlying network may drop, duplicate, or arbitrarily delay messages (see
[“Unreliable Networks”](ch08.html#sec_distributed_networks)), Pregel implementations guarantee that messages are processed exactly
once at their destination vertex in the following iteration. Like MapReduce, the framework
transparently recovers from faults in order to simplify the programming model for algorithms on top
of Pregel.