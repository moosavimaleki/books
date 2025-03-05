At times when the network is working correctly, a system can provide both consistency
(linearizability) and total availability. When a network fault occurs, you have to choose between
either linearizability or total availability. Thus, a better way of phrasing CAP would be
either Consistent or Available when Partitioned
[[39](ch09.html#Cockcroft2014wv)]. A more reliable network needs to
make this choice less often, but at some point the choice is inevitable. In discussions of CAP there are several contradictory definitions of the term availability, and
the formalization as a theorem [[30](ch09.html#Gilbert2002il)] does not
match its usual meaning [[40](ch09.html#Kleppmann2015vp)]. Many
so-called “highly available” (fault-tolerant) systems actually do not meet CAP’s idiosyncratic
definition of availability. All in all, there is a lot of misunderstanding and confusion around CAP,
and it does not help us understand systems better, so CAP is best avoided. 
The CAP theorem as formally defined [[30](ch09.html#Gilbert2002il)] is
of very narrow scope: it only considers one consistency model (namely linearizability) and one kind
of fault (network partitions,[vi](ch09.html#idm140605759746016) or nodes that
are alive but disconnected from each other). It doesn’t say anything about network delays, dead
nodes, or other trade-offs. Thus, although CAP has been historically influential, it has little
practical value for designing systems [[9](ch09.html#Kleppmann2015un),
[40](ch09.html#Kleppmann2015vp)].