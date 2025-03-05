
The rate of aborts significantly affects the overall performance of SSI. For example, a transaction
that reads and writes data over a long period of time is likely to run into conflicts and abort, so
SSI requires that read-write transactions be fairly short (long-running read-only transactions may
be okay). However, SSI is probably less sensitive to slow transactions than two-phase locking or
serial execution. # Summary 
Transactions are an abstraction layer that allows an application to pretend that certain concurrency
problems and certain kinds of hardware and software faults don’t exist. A large class of errors is
reduced down to a simple transaction abort, and the application just needs to try again. In this chapter we saw many examples of problems that transactions help prevent. Not all
applications are susceptible to all those problems: an application with very simple access patterns,
such as reading and writing only a single record, can probably manage without transactions. However,
for more complex access patterns, transactions can hugely reduce the number of potential error cases
you need to think about.