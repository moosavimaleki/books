Such a distributed transaction is only possible if all systems affected by the transaction are able
to use the same atomic commit protocol, however. For example, say a side effect of processing a
message is to send an email, and the email server does not support two-phase commit: it could happen
that the email is sent two or more times if message processing fails and is retried. But if all side
effects of processing a message are rolled back on transaction abort, then the processing step can
safely be retried as if nothing had happened. We will return to the topic of exactly-once message processing in [Chapter 11](ch11.html#ch_stream). Let’s look first at
the atomic commit protocol that allows such heterogeneous distributed transactions. ### XA transactions X/Open XA (short for eXtended Architecture) is a standard for implementing two-phase commit
across heterogeneous technologies [[76](ch09.html#XASpec1991vk),
[77](ch09.html#Spille2004vr)]. It was introduced in 1991 and has been widely
implemented: XA is supported by many traditional relational databases (including PostgreSQL, MySQL,
DB2, SQL Server, and Oracle) and message brokers (including ActiveMQ, HornetQ, MSMQ, and IBM MQ).