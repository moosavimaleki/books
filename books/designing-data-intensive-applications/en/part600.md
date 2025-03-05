Discussions of these systems border on the philosophical: What do we know to be true or false in our
system? How sure can we be of that knowledge, if the mechanisms for perception and measurement are
unreliable? Should software systems obey the laws that we expect of the physical world, such as
cause and effect? 
Fortunately, we don’t need to go as far as figuring out the meaning of life. In a distributed
system, we can state the assumptions we are making about the behavior (the system model) and
design the actual system in such a way that it meets those assumptions. Algorithms can be proved to
function correctly within a certain system model. This means that reliable behavior is achievable,
even if the underlying system model provides very few guarantees. However, although it is possible to make software well behaved in an unreliable system model, it
is not straightforward to do so. In the rest of this chapter we will further explore the notions of
knowledge and truth in distributed systems, which will help us think about the kinds of assumptions
we can make and the guarantees we may want to provide. In [Chapter 9](ch09.html#ch_consistency) we will proceed to
look at some examples of distributed systems, algorithms that provide particular guarantees
under particular assumptions.