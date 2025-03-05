Unfortunately, humans are very slow to make up their minds and respond. If a database transaction
needs to wait for input from a user, the database needs to support a potentially huge number of
concurrent transactions, most of them idle. Most databases cannot do that efficiently, and so almost
all OLTP applications keep transactions short by avoiding interactively waiting for a user within a
transaction. On the web, this means that a transaction is committed within the same HTTP request—a
transaction does not span multiple requests. A new HTTP request starts a new transaction. Even though the human has been taken out of the critical path, transactions have continued to be
executed in an interactive client/server style, one statement at a time. An application makes a
query, reads the result, perhaps makes another query depending on the result of the first query, and
so on. The queries and results are sent back and forth between the application code (running on one
machine) and the database server (on another machine).