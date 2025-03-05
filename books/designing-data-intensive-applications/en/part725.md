Database-internal distributed transactions 
Some distributed databases (i.e., databases that use replication and partitioning in their standard
configuration) support internal transactions among the nodes of that database. For example,
VoltDB and MySQL Cluster’s NDB storage engine have such internal transaction
support. In this case, all the nodes participating in the transaction are running the same
database software. Heterogeneous distributed transactions 
In a heterogeneous transaction, the participants are two or more different technologies: for
example, two databases from different vendors, or even non-database systems such as message
brokers. A distributed transaction across these systems must ensure atomic commit, even though
the systems may be entirely different under the hood. Database-internal transactions do not have to be compatible with any other system, so they can
use any protocol and apply optimizations specific to that particular technology. For that reason,
database-internal distributed transactions can often work quite well. On the other hand,
transactions spanning heterogeneous technologies are a lot more challenging.