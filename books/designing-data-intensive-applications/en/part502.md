![ddia 0709](assets/ddia_0709.png) ###### Figure 7-9. The difference between an interactive transaction and a stored procedure (using the example transaction of [Figure 7-8](#fig_transactions_write_skew)). ### Pros and cons of stored procedures 
Stored procedures have existed for some time in relational databases, and they have been part of the
SQL standard (SQL/PSM) since 1999. They have gained a somewhat bad reputation, for various reasons: *  
Each database vendor has its own language for stored procedures (Oracle has PL/SQL, SQL Server
has T-SQL, PostgreSQL has PL/pgSQL, etc.). These languages haven’t kept up with developments in
general-purpose programming languages, so they look quite ugly and archaic from today’s point of
view, and they lack the ecosystem of libraries that you find with most programming languages. *  Code running in a database is difficult to manage: compared to an application server, it’s harder
to debug, more awkward to keep in version control and deploy, trickier to test, and difficult to
integrate with a metrics collection system for monitoring.