*  In the CAP theorem (see [Chapter 9](ch09.html#ch_consistency)), the word consistency is used to mean
linearizability (see [“Linearizability”](ch09.html#sec_consistency_linearizability)). *  In the context of ACID, consistency refers to an application-specific notion of the database
being in a “good state.” It’s unfortunate that the same word is used with at least four different meanings. 
The idea of ACID consistency is that you have certain statements about your data (invariants) that
must always be true—for example, in an accounting system, credits and debits across all accounts
must always be balanced. If a transaction starts with a database that is valid according to these
invariants, and any writes during the transaction preserve the validity, then you can be sure that
the invariants are always satisfied. 
However, this idea of consistency depends on the application’s notion of invariants, and it’s the
application’s responsibility to define its transactions correctly so that they preserve consistency.
This is not something that the database can guarantee: if you write bad data that violates your
invariants, the database can’t stop you. (Some specific kinds of invariants can be checked by the
database, for example using foreign key constraints or uniqueness constraints. However, in general,
the application defines what data is valid or invalid—the database only stores it.)