
We also came across the state machine replication principle in [“Total Order Broadcast”](ch09.html#sec_consistency_total_order),
which states: if every event represents a write to the database, and every replica processes the
same events in the same order, then the replicas will all end up in the same final state.
(Processing an event is assumed to be a deterministic operation.) It’s just another case of event
streams! In this section we will first look at a problem that arises in heterogeneous data systems, and then
explore how we can solve it by bringing ideas from event streams to databases. ## Keeping Systems in Sync 
As we have seen throughout this book, there is no single system that can satisfy all data storage,
querying, and processing needs. In practice, most nontrivial applications need to combine
several different technologies in order to satisfy their requirements: for example, using an OLTP
database to serve user requests, a cache to speed up common requests, a full-text index to handle
search queries, and a data warehouse for analytics. Each of these has its own copy of the data,
stored in its own representation that is optimized for its own purposes.