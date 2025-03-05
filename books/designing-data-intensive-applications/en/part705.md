*  
You can make your read from a replica that is synchronously updated on writes, and is thus sure
to be up to date. (This technique is used in chain replication
[[63](ch09.html#vanRenesse2004td)]; see also [“Research on Replication”](ch05.html#sidebar_replication_research).) ### Implementing total order broadcast using linearizable storage 
The last section showed how to build a linearizable compare-and-set operation from total order
broadcast. We can also turn it around, assume that we have linearizable storage, and show how to
build total order broadcast from it. 
The easiest way is to assume you have a linearizable register that stores an integer and that has an
atomic increment-and-get operation [[28](ch09.html#Herlihy1991gk)].
Alternatively, an atomic compare-and-set operation would also do the job. The algorithm is simple: for every message you want to send through total order broadcast, you
increment-and-get the linearizable integer, and then attach the value you got from the register as a
sequence number to the message. You can then send the message to all nodes (resending any lost
messages), and the recipients will deliver the messages consecutively by sequence number.