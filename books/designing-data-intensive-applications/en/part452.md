[Figure 7-3](#fig_transactions_atomicity) illustrates the need for atomicity: if an error occurs somewhere
over the course of the transaction, the contents of the mailbox and the unread counter might become out
of sync. In an atomic transaction, if the update to the counter fails, the transaction is aborted
and the inserted email is rolled back. ![ddia 0703](assets/ddia_0703.png) ###### Figure 7-3. Atomicity ensures that if an error occurs any prior writes from that transaction are undone, to avoid an inconsistent state. 
Multi-object transactions require some way of determining which read and write operations belong to
the same transaction. In relational databases, that is typically done based on the client’s TCP
connection to the database server: on any particular connection, everything between a BEGIN
TRANSACTION and a COMMIT statement is considered to be part of the same
transaction.[iii](ch07.html#idm140605774697856) On the other hand, many nonrelational databases don’t have such a way of grouping operations
together. Even if there is a multi-object API (for example, a key-value store may have a multi-put
operation that updates several keys in one operation), that doesn’t necessarily mean it has
transaction semantics: the command may succeed for some keys and fail for others, leaving the
database in a partially updated state.