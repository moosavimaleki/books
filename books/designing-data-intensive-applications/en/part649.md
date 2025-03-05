
In a linearizable system, as soon as one client successfully completes a write, all clients reading
from the database must be able to see the value just written. Maintaining the illusion of a single
copy of the data means guaranteeing that the value read is the most recent, up-to-date value, and
doesn’t come from a stale cache or replica. In other words, linearizability is a recency
guarantee. To clarify this idea, let’s look at an example of a system that is not linearizable. ![ddia 0901](assets/ddia_0901.png) ###### Figure 9-1. This system is not linearizable, causing football fans to be confused. [Figure 9-1](#fig_consistency_linearizability_0) shows an example of a nonlinearizable sports website
[[9](ch09.html#Kleppmann2015un)].
Alice and Bob are sitting in the same room, both checking their phones to see the outcome of the
2014 FIFA World Cup final. Just after the final score is announced, Alice refreshes the page,
sees the winner announced, and excitedly tells Bob about it. Bob incredulously hits reload on his
own phone, but his request goes to a database replica that is lagging, and so his phone shows that
the game is still ongoing.