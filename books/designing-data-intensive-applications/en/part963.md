### Message passing and RPC 
In [“Message-Passing Dataflow”](ch04.html#sec_encoding_dataflow_msg) we discussed message-passing systems as an alternative to RPC—i.e.,
as a mechanism for services to communicate, as used for example in the actor model. Although these
systems are also based on messages and events, we normally don’t think of them as stream processors: *  Actor frameworks are primarily a mechanism for managing concurrency and distributed execution of
communicating modules, whereas stream processing is primarily a data management technique. *  Communication between actors is often ephemeral and one-to-one, whereas event logs are durable and
multi-subscriber. *  Actors can communicate in arbitrary ways (including cyclic request/response patterns), but stream
processors are usually set up in acyclic pipelines where every stream is the output of one
particular job, and derived from a well-defined set of input streams. 
That said, there is some crossover area between RPC-like systems and stream processing. For
example, Apache Storm has a feature called distributed RPC, which allows user queries to be farmed
out to a set of nodes that also process event streams; these queries are then interleaved with
events from the input streams, and results can be aggregated and sent back to the user
[[78](ch11.html#StormDocs)].
(See also [“Multi-partition data processing”](ch12.html#sec_future_unbundled_multi_partition).)