```
`BEGIN`` ``TRANSACTION``;``

``SELECT`` ``*`` ``FROM`` ``figures``
  ``WHERE`` ``name`` ``=`` ``'robot'`` ``AND`` ``game_id`` ``=`` ``222``
  ``FOR`` ``UPDATE``;`` `[![1](assets/1.png)](#callout_transactions_CO1-1)`

``-- Check whether move is valid, then update the position
``-- of the piece that was returned by the previous SELECT.
``UPDATE`` ``figures`` ``SET`` ``position`` ``=`` ``'c4'`` ``WHERE`` ``id`` ``=`` ``1234``;``

``COMMIT``;`
``` [![1](assets/1.png)](#co_transactions_CO1-1) The FOR UPDATE clause indicates that the database should take a lock on all rows returned by
this query. This works, but to get it right, you need to carefully think about your application logic. It’s easy
to forget to add a necessary lock somewhere in the code, and thus introduce a race condition. ### Automatically detecting lost updates 
Atomic operations and locks are ways of preventing lost updates by forcing the read-modify-write
cycles to happen sequentially. An alternative is to allow them to execute in parallel and, if the
transaction manager detects a lost update, abort the transaction and force it to retry
its read-modify-write cycle.