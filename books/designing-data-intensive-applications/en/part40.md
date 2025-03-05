# Scalability 
Even if a system is working reliably today, that doesn’t mean it will necessarily work reliably in
the future. One common reason for degradation is increased load: perhaps the system has grown from 10,000
concurrent users to 100,000 concurrent users, or from 1 million to 10 million. Perhaps it is
processing much larger volumes of data than it did before. Scalability is the term we use to describe a system’s ability to cope with increased load. Note,
however, that it is not a one-dimensional label that we can attach to a system: it is meaningless to
say “X is scalable” or “Y doesn’t scale.” Rather, discussing scalability means considering questions
like “If the system grows in a particular way, what are our options for coping with the growth?” and
“How can we add computing resources to handle the additional load?” ## Describing Load 
First, we need to succinctly describe the current load on the system; only then can we discuss
growth questions (what happens if our load doubles?). Load can be described with a few numbers which
we call load parameters. The best choice of parameters depends on the architecture of your
system: it may be requests per second to a web server, the ratio of reads to writes in a database, the
number of simultaneously active users in a chat room, the hit rate on a cache, or something else.
Perhaps the average case is what matters for you, or perhaps your bottleneck is dominated by a small
number of extreme cases.