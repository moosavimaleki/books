
An advantage of this approach is that databases can perform this check efficiently in conjunction
with snapshot isolation. Indeed, PostgreSQL’s repeatable read, Oracle’s serializable, and SQL
Server’s snapshot isolation levels automatically detect when a lost update has occurred and abort
the offending transaction. However, MySQL/InnoDB’s repeatable read does not detect lost updates
[[23](ch07.html#Kleppmann2014ut)]. Some authors
[[28](ch07.html#Berenson1995kj),
[30](ch07.html#Bailis2014vc_ch7)] argue that a database must prevent lost
updates in order to qualify as providing snapshot isolation, so MySQL does not provide snapshot
isolation under this definition. Lost update detection is a great feature, because it doesn’t require application code to use any
special database features—you may forget to use a lock or an atomic operation and thus introduce
a bug, but lost update detection happens automatically and is thus less error-prone. ### Compare-and-set 
In databases that don’t provide transactions, you sometimes find an atomic compare-and-set operation
(previously mentioned in [“Single-object writes”](#sec_transactions_single_object)). The purpose of this operation is to
avoid lost updates by allowing an update to happen only if the value has not changed since you last
read it. If the current value does not match what you previously read, the update has no effect, and
the read-modify-write cycle must be retried.