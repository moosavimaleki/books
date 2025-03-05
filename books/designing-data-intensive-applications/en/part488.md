You can think of write skew as a generalization of the lost update problem. Write skew can occur if two
transactions read the same objects, and then update some of those objects (different transactions
may update different objects). In the special case where different transactions update the same
object, you get a dirty write or lost update anomaly (depending on the timing). 
We saw that there are various different ways of preventing lost updates. With write skew, our
options are more restricted: *  Atomic single-object operations don’t help, as multiple objects are involved. *  
The automatic detection of lost updates that you find in some implementations of snapshot
isolation unfortunately doesn’t help either: write skew is not automatically detected in
PostgreSQL’s repeatable read, MySQL/InnoDB’s repeatable read, Oracle’s serializable, or SQL
Server’s snapshot isolation level [[23](ch07.html#Kleppmann2014ut)].
Automatically preventing write skew requires true serializable isolation (see
[“Serializability”](#sec_transactions_serializability)). *  
Some databases allow you to configure constraints, which are then enforced by the database (e.g.,
uniqueness, foreign key constraints, or restrictions on a particular value). However, in order to
specify that at least one doctor must be on call, you would need a constraint that involves
multiple objects. Most databases do not have built-in support for such constraints, but you may be
able to implement them with triggers or materialized views, depending on the database
[[42](ch07.html#Andrews2004wp)].