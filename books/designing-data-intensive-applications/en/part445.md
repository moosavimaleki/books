Atomicity, isolation, and durability are properties of the database, whereas consistency (in the ACID
sense) is a property of the application. The application may rely on the database’s atomicity and
isolation properties in order to achieve consistency, but it’s not up to the database alone. Thus,
the letter C doesn’t really belong in ACID.[i](ch07.html#idm140605774826704) ### Isolation 
Most databases are accessed by several clients at the same time. That is no problem if they are
reading and writing different parts of the database, but if they are accessing the same database
records, you can run into concurrency problems (race conditions). [Figure 7-1](#fig_transactions_increment) is a simple example of this kind of problem. Say you have two clients
simultaneously incrementing a counter that is stored in a database. Each client needs to read the
current value, add 1, and write the new value back (assuming there is no increment operation built
into the database). In [Figure 7-1](#fig_transactions_increment) the counter should have increased from 42 to
44, because two increments happened, but it actually only went to 43 because of the race condition.