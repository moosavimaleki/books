Rather than blindly relying on tools, we need to develop a good understanding of the kinds of
concurrency problems that exist, and how to prevent them. Then we can build applications that are
reliable and correct, using the tools at our disposal. In this section we will look at several weak (nonserializable) isolation levels that are used in
practice, and discuss in detail what kinds of race conditions can and cannot occur, so that you can
decide what level is appropriate to your application. Once we’ve done that, we will discuss
serializability in detail (see [“Serializability”](#sec_transactions_serializability)). Our discussion of isolation
levels will be informal, using examples. If you want rigorous definitions and analyses of their
properties, you can find them in the academic literature
[[28](ch07.html#Berenson1995kj),
[29](ch07.html#Adya1999tx),
[30](ch07.html#Bailis2014vc_ch7)]. ## Read Committed 
The most basic level of transaction isolation is
read committed.[v](ch07.html#idm140605774566176) It makes two guarantees: 1.  When reading from the database, you will only see data that has been committed (no dirty
reads).