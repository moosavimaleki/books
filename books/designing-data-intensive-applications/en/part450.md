## Single-Object and Multi-Object Operations 
To recap, in ACID, atomicity and isolation describe what the database should do if a client makes
several writes within the same transaction: Atomicity If an error occurs halfway through a sequence of writes, the transaction should be aborted, and
the writes made up to that point should be discarded. In other words, the database saves you from
having to worry about partial failure, by giving an all-or-nothing guarantee. Isolation Concurrently running transactions shouldn’t interfere with each other. For example, if one
transaction makes several writes, then another transaction should see either all or none of those
writes, but not some subset. 
These definitions assume that you want to modify several objects (rows, documents, records) at once.
Such multi-object transactions are often needed if several pieces of data need to be kept in sync.
[Figure 7-2](#fig_transactions_read_uncommitted) shows an example from an email application. To display the
number of unread messages for a user, you could query something like: