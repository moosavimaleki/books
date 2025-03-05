If Alice and Bob had hit reload at the same time, it would have been less surprising if they had gotten
two different query results, because they wouldn’t know at exactly what time their respective requests
were processed by the server. However, Bob knows that he hit the reload button (initiated his query)
after he heard Alice exclaim the final score, and therefore he expects his query result to be at
least as recent as Alice’s. The fact that his query returned a stale result is a violation of
linearizability. ## What Makes a System Linearizable? 
The basic idea behind linearizability is simple: to make a system appear as if there is only a single
copy of the data. However, nailing down precisely what that means actually requires some care. In
order to understand linearizability better, let’s look at some more examples. [Figure 9-2](#fig_consistency_linearizability_1) shows three clients concurrently reading and writing the same
key x in a linearizable database. In the distributed systems literature, x is called a
register—in practice, it could be one key in a key-value store, one row in a relational
database, or one document in a document database, for example.