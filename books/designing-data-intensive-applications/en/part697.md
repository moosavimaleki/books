In order to be sure that no other node is in the process of concurrently creating an account with
the same username and a lower timestamp, you would have to check with every other node to see what
it is doing [[56](ch09.html#Lamport1978jq_ch9)].
If one of the other nodes has failed or cannot be reached due to a network problem, this system
would grind to a halt. This is not the kind of fault-tolerant system that we need. The problem here is that the total order of operations only emerges after you have collected all of
the operations. If another node has generated some operations, but you don’t yet know what they are,
you cannot construct the final ordering of operations: the unknown operations from the other node
may need to be inserted at various positions in the total order. 
To conclude: in order to implement something like a uniqueness constraint for usernames, it’s not
sufficient to have a total ordering of operations—you also need to know when that order is
finalized. If you have an operation to create a username, and you are sure that no other node can
insert a claim for the same username ahead of your operation in the total order, then you can safely
declare the operation successful.