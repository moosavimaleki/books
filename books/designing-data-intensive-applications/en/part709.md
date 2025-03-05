##### The Impossibility of Consensus 
You may have heard about the FLP result
[[68](ch09.html#Fischer1985ji)]—named after the
authors Fischer, Lynch, and Paterson—which proves that there is no algorithm that is always able to
reach consensus if there is a risk that a node may crash. In a distributed system, we must assume
that nodes may crash, so reliable consensus is impossible. Yet, here we are, discussing algorithms
for achieving consensus. What is going on here? The answer is that the FLP result is proved in the asynchronous system model (see
[“System Model and Reality”](ch08.html#sec_distributed_system_model)), a very restrictive model that assumes a deterministic algorithm
that cannot use any clocks or timeouts. If the algorithm is allowed to use timeouts, or some other
way of identifying suspected crashed nodes (even if the suspicion is sometimes wrong), then
consensus becomes solvable [[67](ch09.html#Chandra1996cp)]. Even just
allowing the algorithm to use random numbers is sufficient to get around the impossibility result
[[69](ch09.html#BenOr1983dh)].