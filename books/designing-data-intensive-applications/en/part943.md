## State, Streams, and Immutability 
We saw in [Chapter 10](ch10.html#ch_batch) that batch processing benefits from the immutability of its input files, so
you can run experimental processing jobs on existing input files without fear of damaging them. This
principle of immutability is also what makes event sourcing and change data capture so powerful. 
We normally think of databases as storing the current state of the application—this
representation is optimized for reads, and it is usually the most convenient for serving queries.
The nature of state is that it changes, so databases support updating and deleting data as
well as inserting it. How does this fit with immutability? Whenever you have state that changes, that state is the result of the events that mutated it over
time. For example, your list of currently available seats is the result of the reservations you have
processed, the current account balance is the result of the credits and debits on the account, and
the response time graph for your web server is an aggregation of the individual response times of
all web requests that have occurred.