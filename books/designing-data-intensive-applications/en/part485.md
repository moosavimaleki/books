
Atomic operations can work well in a replicated context, especially if they are commutative (i.e.,
you can apply them in a different order on different replicas, and still get the same result). For
example, incrementing a counter or adding an element to a set are commutative operations. That is
the idea behind Riak 2.0 datatypes, which prevent lost updates across replicas. When a value is
concurrently updated by different clients, Riak automatically merges together the updates in such a
way that no updates are lost [[39](ch07.html#Jacobson2014wa_ch7)]. 
On the other hand, the last write wins (LWW) conflict resolution method is prone to lost updates,
as discussed in [“Last write wins (discarding concurrent writes)”](ch05.html#sec_replication_lww). Unfortunately, LWW is the default in many replicated
databases. ## Write Skew and Phantoms 
In the previous sections we saw dirty writes and lost updates, two kinds of race conditions that
can occur when different transactions concurrently try to write to the same objects. In order to
avoid data corruption, those race conditions need to be prevented—either automatically by the
database, or by manual safeguards such as using locks or atomic write operations.