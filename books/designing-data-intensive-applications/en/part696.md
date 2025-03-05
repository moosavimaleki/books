For example, consider a system that needs to ensure that a username uniquely identifies a user
account. If two users concurrently try to create an account with the same username, one of the two
should succeed and the other should fail. (We touched on this problem previously in
[“The leader and the lock”](ch08.html#sec_distributed_lock_fencing).) At first glance, it seems as though a total ordering of operations (e.g., using Lamport timestamps)
should be sufficient to solve this problem: if two accounts with the same username are created, pick
the one with the lower timestamp as the winner (the one who grabbed the username first), and let the
one with the greater timestamp fail. Since timestamps are totally ordered, this comparison is always
valid. This approach works for determining the winner after the fact: once you have collected all the
username creation operations in the system, you can compare their timestamps. However, it is not
sufficient when a node has just received a request from a user to create a username, and needs to
decide right now whether the request should succeed or fail. At that moment, the node does not
know whether another node is concurrently in the process of creating an account with the same
username, and what timestamp that other node may assign to the operation.