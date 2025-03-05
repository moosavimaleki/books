
This approach is called materializing conflicts, because it takes a phantom and turns it into a
lock conflict on a concrete set of rows that exist in the database
[[11](ch07.html#Fekete2005ee)]. Unfortunately, it can be hard and
error-prone to figure out how to materialize conflicts, and it’s ugly to let a concurrency control
mechanism leak into the application data model. For those reasons, materializing conflicts should be
considered a last resort if no alternative is possible. A serializable isolation level is much
preferable in most cases. # Serializability 
In this chapter we have seen several examples of transactions that are prone to race conditions.
Some race conditions are prevented by the read committed and snapshot isolation levels, but
others are not. We encountered some particularly tricky examples with write skew and phantoms. It’s
a sad situation: *  Isolation levels are hard to understand, and inconsistently implemented in different databases
(e.g., the meaning of “repeatable read” varies significantly).