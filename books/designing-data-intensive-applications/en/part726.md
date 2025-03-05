### Exactly-once message processing 
Heterogeneous distributed transactions allow diverse systems to be integrated in powerful ways. For
example, a message from a message queue can be acknowledged as processed if and only if the database
transaction for processing the message was successfully committed. This is implemented by atomically
committing the message acknowledgment and the database writes in a single transaction. With
distributed transaction support, this is possible, even if the message broker and the database are
two unrelated technologies running on different machines. If either the message delivery or the database transaction fails, both are aborted, and so the
message broker may safely redeliver the message later. Thus, by atomically committing the message
and the side effects of its processing, we can ensure that the message is effectively processed
exactly once, even if it required a few retries before it succeeded. The abort discards any
side effects of the partially completed transaction.