Uniqueness No two requests for a fencing token return the same value. Monotonic sequence If request x returned token tx, and request y returned token ty, and
x completed before y began, then tx < ty. Availability A node that requests a fencing token and does not crash eventually receives a response. An algorithm is correct in some system model if it always satisfies its properties in all situations
that we assume may occur in that system model. But how does this make sense? If all nodes crash, or
all network delays suddenly become infinitely long, then no algorithm will be able to get anything
done. ### Safety and liveness 
To clarify the situation, it is worth distinguishing between two different kinds of properties:
safety and liveness properties. In the example just given, uniqueness and monotonic sequence are
safety properties, but availability is a liveness property. 
What distinguishes the two kinds of properties? A giveaway is that liveness properties often include
the word “eventually” in their definition. (And yes, you guessed it—eventual consistency is a
liveness property [[89](ch08.html#Bailis2013jc_ch8)].)