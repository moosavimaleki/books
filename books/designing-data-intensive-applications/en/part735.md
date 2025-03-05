The consensus problem is normally formalized as follows: one or more nodes may propose values, and
the consensus algorithm decides on one of those values. In the seat-booking example, when several
customers are concurrently trying to buy the last seat, each node handling a customer request may
propose the ID of the customer it is serving, and the decision indicates which one of those
customers got the seat. 
In this formalism, a consensus algorithm must satisfy the following properties
[[25](ch09.html#Cachin2011wt)]:[xiii](ch09.html#idm140605759010832) Uniform agreement 
No two nodes decide differently. Integrity 
No node decides twice. Validity 
If a node decides value v, then v was proposed by some node. Termination 
Every node that does not crash eventually decides some value. The uniform agreement and integrity properties define the core idea of consensus: everyone decides
on the same outcome, and once you have decided, you cannot change your mind. The validity property
exists mostly to rule out trivial solutions: for example, you could have an algorithm that always
decides null, no matter what was proposed; this algorithm would satisfy the agreement and
integrity properties, but not the validity property.