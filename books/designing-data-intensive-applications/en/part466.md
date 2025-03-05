How do we prevent dirty reads? One option would be to use the same lock, and to require any
transaction that wants to read an object to briefly acquire the lock and then release it again
immediately after reading. This would ensure that a read couldn’t happen while an object has a
dirty, uncommitted value (because during that time the lock would be held by the transaction that
has made the write). 
However, the approach of requiring read locks does not work well in practice, because one
long-running write transaction can force many read-only transactions to wait until the long-running
transaction has completed. This harms the response time of read-only transactions and is bad for
operability: a slowdown in one part of an application can have a knock-on effect in a completely
different part of the application, due to waiting for locks. For that reason, most databases[vi](ch07.html#idm140605774512368)
prevent dirty reads using the approach illustrated in [Figure 7-4](#fig_transactions_read_committed): for every
object that is written, the database remembers both the old committed value and the new value
set by the transaction that currently holds the write lock. While the transaction is ongoing, any
other transactions that read the object are simply given the old value. Only when the new value is
committed do transactions switch over to reading the new value.