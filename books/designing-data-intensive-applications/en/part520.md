Put another way, the transaction is taking an action based on a premise (a fact that was true at
the beginning of the transaction, e.g., “There are currently two doctors on call”). Later, when the
transaction wants to commit, the original data may have changed—the premise may no longer be
true. 
When the application makes a query (e.g., “How many doctors are currently on call?”), the database
doesn’t know how the application logic uses the result of that query. To be safe, the database needs
to assume that any change in the query result (the premise) means that writes in that transaction
may be invalid. In other words, there may be a causal dependency between the queries and the writes
in the transaction. In order to provide serializable isolation, the database must detect situations
in which a transaction may have acted on an outdated premise and abort the transaction in that case.