## The Meaning of ACID 
The safety guarantees provided by transactions are often described by the well-known acronym ACID,
which stands for Atomicity, Consistency, Isolation, and Durability. It was coined in 1983 by
Theo Härder and Andreas Reuter [[7](ch07.html#Harder1983cu)]
in an effort to establish precise terminology for fault-tolerance mechanisms in databases. However, in practice, one database’s implementation of ACID does not equal another’s implementation.
For example, as we shall see, there is a lot of ambiguity around the meaning of isolation
[[8](ch07.html#Bailis2013tn)].
The high-level idea is sound, but the devil is in the details. Today, when a system claims to be
“ACID compliant,” it’s unclear what guarantees you can actually expect. ACID has unfortunately
become mostly a marketing term. 
(Systems that do not meet the ACID criteria are sometimes called BASE, which stands for
Basically Available, Soft state, and Eventual consistency
[[9](ch07.html#Fox1997wj)].
This is even more vague than the definition of ACID. It seems that the only sensible definition of
BASE is “not ACID”; i.e., it can mean almost anything you want.)