*  Many server-side applications are developed in a stateless model (as favored by HTTP), with all
persistent state stored in a database, which has the advantage that application servers can be
added and removed at will. However, when the coordinator is part of the application server, it
changes the nature of the deployment. Suddenly, the coordinator’s logs become a crucial part of the
durable system state—as important as the databases themselves, since the coordinator logs are
required in order to recover in-doubt transactions after a crash. Such application servers are no
longer stateless. *  
Since XA needs to be compatible with a wide range of data systems, it is necessarily a lowest
common denominator. For example, it cannot detect deadlocks across different systems (since that
would require a standardized protocol for systems to exchange information on the locks that each
transaction is waiting for), and it does not work with SSI (see [“Serializable Snapshot Isolation (SSI)”](ch07.html#sec_transactions_ssi)), since
that would require a protocol for identifying conflicts across different systems.