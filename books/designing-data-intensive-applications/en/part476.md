### Repeatable read and naming confusion 
Snapshot isolation is a useful isolation level, especially for read-only transactions. However, many
databases that implement it call it by different names. In Oracle it is called serializable, and
in PostgreSQL and MySQL it is called repeatable read
[[23](ch07.html#Kleppmann2014ut)]. The reason for this naming confusion is that the SQL standard doesn’t have the concept of snapshot
isolation, because the standard is based on System R’s 1975 definition of isolation levels
[[2](ch07.html#Gray1976us)] and snapshot isolation hadn’t yet been
invented then. Instead, it defines repeatable read, which looks superficially similar to snapshot
isolation. PostgreSQL and MySQL call their snapshot isolation level repeatable read because it
meets the requirements of the standard, and so they can claim standards compliance. 
Unfortunately, the SQL standard’s definition of isolation levels is flawed—it is ambiguous,
imprecise, and not as implementation-independent as a standard should be
[[28](ch07.html#Berenson1995kj)]. Even though several databases
implement repeatable read, there are big differences in the guarantees they actually provide,
despite being ostensibly standardized
[[23](ch07.html#Kleppmann2014ut)]. There has been a formal definition of
repeatable read in the research literature [[29](ch07.html#Adya1999tx),
[30](ch07.html#Bailis2014vc_ch7)], but most implementations don’t satisfy that
formal definition. And to top it off, IBM DB2 uses “repeatable read” to refer to serializability
[[8](ch07.html#Bailis2013tn)].