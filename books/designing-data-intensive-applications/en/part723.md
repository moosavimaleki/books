### Three-phase commit 
Two-phase commit is called a blocking atomic commit protocol due to the fact that 2PC can become
stuck waiting for the coordinator to recover. In theory, it is possible to make an atomic commit
protocol nonblocking, so that it does not get stuck if a node fails. However, making this work in
practice is not so straightforward. As an alternative to 2PC, an algorithm called three-phase commit (3PC) has been proposed
[[13](ch09.html#Bernstein1987va_ch9),
[80](ch09.html#Skeen1981jc)].
However, 3PC assumes a network with bounded delay and nodes with bounded response times; in most
practical systems with unbounded network delay and process pauses (see [Chapter 8](ch08.html#ch_distributed)), it
cannot guarantee atomicity. 
In general, nonblocking atomic commit requires a perfect failure detector
[[67](ch09.html#Chandra1996cp),
[71](ch09.html#Guerraoui1995bi)]—i.e., a reliable mechanism for telling
whether a node has crashed or not. In a network with unbounded delay a timeout is not a reliable
failure detector, because a request may time out due to a network problem even if no node has
crashed. For this reason, 2PC continues to be used, despite the known problem with coordinator
failure.