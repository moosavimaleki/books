Thus, applications that don’t require linearizability can be more tolerant of network problems. This
insight is popularly known as the CAP theorem
[[29](ch09.html#Fox1999bs),
[30](ch09.html#Gilbert2002il),
[31](ch09.html#Gilbert2012bf),
[32](ch09.html#Brewer2012ba)],
named by Eric Brewer in 2000, although the trade-off has been known to designers of
distributed databases since the 1970s
[[33](ch09.html#Davidson1985hv),
[34](ch09.html#Johnson1975we),
[35](ch09.html#Lindsay1979wv_ch9),
[36](ch09.html#Fischer1982hc)]. CAP was originally proposed as a rule of thumb, without precise definitions, with the goal of
starting a discussion about trade-offs in databases. At the time, many distributed databases
focused on providing linearizable semantics on a cluster of machines with shared storage
[[18](ch09.html#Vallath2006ut)], and CAP encouraged database engineers
to explore a wider design space of distributed shared-nothing systems, which were more suitable for
implementing large-scale web services [[37](ch09.html#Brewer2012tr)].
CAP deserves credit for this culture shift—witness the explosion of new database technologies
since the mid-2000s (known as NoSQL). ##### The Unhelpful CAP Theorem CAP is sometimes presented as Consistency, Availability, Partition tolerance: pick 2 out of 3.
Unfortunately, putting it this way is misleading
[[32](ch09.html#Brewer2012ba)] because network partitions are a kind of
fault, so they aren’t something about which you have a choice: they will happen whether you like it or not
[[38](ch09.html#Robinson2010tp)].