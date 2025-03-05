### The Pregel processing model 
As an optimization for batch processing graphs, the bulk synchronous parallel (BSP) model of
computation [[70](ch10.html#Valiant1990ce)]
has become popular. Among others, it is implemented by Apache Giraph
[[37](ch10.html#Grover2015tl)], Spark’s GraphX API, and Flink’s Gelly API
[[71](ch10.html#Ewen2012cm)].
It is also known as the Pregel model, as Google’s Pregel paper popularized this approach for
processing graphs [[72](ch10.html#Malewicz2010jq)]. Recall that in MapReduce, mappers conceptually “send a message” to a particular call of the reducer
because the framework collects together all the mapper outputs with the same key. A similar idea is
behind Pregel: one vertex can “send a message” to another vertex, and typically those messages are
sent along the edges in a graph. In each iteration, a function is called for each vertex, passing it all the messages that were sent
to it—much like a call to the reducer. The difference from MapReduce is that in the Pregel
model, a vertex remembers its state in memory from one iteration to the next, so the function only
needs to process new incoming messages. If no messages are being sent in some part of the graph, no
work needs to be done.