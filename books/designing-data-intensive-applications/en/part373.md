An operation A happens before another operation B if B knows about A, or depends on A, or builds
upon A in some way. Whether one operation happens before another operation is the key to defining
what concurrency means. In fact, we can simply say that two operations are concurrent if neither
happens before the other (i.e., neither knows about the other)
[[54](ch05.html#Lamport1978jq_ch5)]. Thus, whenever you have two operations A and B, there are three possibilities: either A happened
before B, or B happened before A, or A and B are concurrent. What we need is an algorithm to tell us
whether two operations are concurrent or not. If one operation happened before another, the later
operation should overwrite the earlier operation, but if the operations are concurrent, we have a
conflict that needs to be resolved. ##### Concurrency, Time, and Relativity 
It may seem that two operations should be called concurrent if they occur “at the same time”—but
in fact, it is not important whether they literally overlap in time. Because of problems with clocks
in distributed systems, it is actually quite difficult to tell whether two things happened
at exactly the same time—an issue we will discuss in more detail in [Chapter 8](ch08.html#ch_distributed).