### Explicit locking 
Another option for preventing lost updates, if the database’s built-in atomic operations don’t
provide the necessary functionality, is for the application to explicitly lock objects that are
going to be updated. Then the application can perform a read-modify-write cycle, and if any other
transaction tries to concurrently read the same object, it is forced to wait until the first
read-modify-write cycle has completed. For example, consider a multiplayer game in which several players can move the same figure
concurrently. In this case, an atomic operation may not be sufficient, because the application also
needs to ensure that a player’s move abides by the rules of the game, which involves some logic that
you cannot sensibly implement as a database query. Instead, you may use a lock to prevent two
players from concurrently moving the same piece, as illustrated in [Example 7-1](#fig_transactions_select_for_update). ##### Example 7-1. Explicitly locking rows to prevent lost updates