*  If you look at your application code, it’s difficult to tell whether it is safe to run at a
particular isolation level—especially in a large application, where you might not be aware of
all the things that may be happening concurrently. *  There are no good tools to help us detect race conditions. In principle, static analysis may
help [[26](ch07.html#Jorwekar2007uq_ch7)],  but research techniques have not
yet found their way into practical use. Testing for concurrency issues is hard, because they are
usually nondeterministic—problems only occur if you get unlucky with the timing. This is not a new problem—it has been like this since the 1970s, when weak isolation levels were
first introduced [[2](ch07.html#Gray1976us)]. All along, the answer
from researchers has been simple: use serializable isolation! 
Serializable isolation is usually regarded as the strongest isolation level. It guarantees that even
though transactions may execute in parallel, the end result is the same as if they had executed one
at a time, serially, without any concurrency. Thus, the database guarantees that if the
transactions behave correctly when run individually, they continue to be correct when run
concurrently—in other words, the database prevents all possible race conditions.