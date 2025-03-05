The examples in this chapter used a relational data model. However, as discussed in
[“The need for multi-object transactions”](#sec_transactions_need), transactions are a valuable database feature, no matter which data model
is used. In this chapter, we explored ideas and algorithms mostly in the context of a database running on a
single machine. Transactions in distributed databases open a new set of difficult challenges, which
we’ll discuss in the next two chapters. ##### Footnotes [i](ch07.html#idm140605774826704-marker) Joe
Hellerstein has remarked that the C in ACID was “tossed in to make the acronym work” in Härder and
Reuter’s paper [[7](ch07.html#Harder1983cu)], and
that it wasn’t considered important at the time. [ii](ch07.html#idm140605774708544-marker) Arguably, an incorrect counter in
an email application is not a particularly critical problem. Alternatively, think of a customer
account balance instead of an unread counter, and a payment transaction instead of an email. [iii](ch07.html#idm140605774697856-marker) This is not ideal. If the TCP
connection is interrupted, the transaction must be aborted. If the interruption happens after the
client has requested a commit but before the server acknowledges that the commit happened, the client
doesn’t know whether the transaction was committed or not. To solve this issue, a transaction manager can group
operations by a unique transaction identifier that is not bound to a particular TCP
connection. We will return to this topic in [“The End-to-End Argument for Databases”](ch12.html#sec_future_end_to_end).