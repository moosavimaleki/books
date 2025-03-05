Using clock synchronization for distributed transaction semantics is an area of active research
[[57](ch08.html#Kulkarni2014ws),
[61](ch08.html#Bravo2015uy),
[62](ch08.html#Kimball2016wi)].
These ideas are interesting, but they have not yet been implemented in mainstream databases outside
of Google. ## Process Pauses 
Let’s consider another example of dangerous clock use in a distributed system. Say you have a
database with a single leader per partition. Only the leader is allowed to accept writes. How does a
node know that it is still leader (that it hasn’t been declared dead by the others), and that it may
safely accept writes? 
One option is for the leader to obtain a lease from the other nodes, which is similar to a lock
with a timeout [[63](ch08.html#Gray1989cu)].
Only one node can hold the lease at any one time—thus, when a node obtains a lease, it knows that
it is the leader for some amount of time, until the lease expires. In order to remain leader, the
node must periodically renew the lease before it expires. If the node fails, it stops renewing the
lease, so another node can take over when it expires.