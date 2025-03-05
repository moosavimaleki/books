
Distributed locking is also used at a much more granular level in some distributed databases, such as
Oracle Real Application Clusters (RAC) [[18](ch09.html#Vallath2006ut)]. RAC uses a lock per disk page, with multiple nodes sharing access
to the same disk storage system. Since these linearizable locks are on the critical path of
transaction execution, RAC deployments usually have a dedicated cluster interconnect network for
communication between database nodes. ### Constraints and uniqueness guarantees 
Uniqueness constraints are common in databases: for example, a username or email address must
uniquely identify one user, and in a file storage service there cannot be two files with the same
path and filename. If you want to enforce this constraint as the data is written (such that if two people
try to concurrently create a user or a file with the same name, one of them will be returned an
error), you need linearizability. 
This situation is actually similar to a lock: when a user registers for your service, you can think
of them acquiring a “lock” on their chosen username. The operation is also very similar to an atomic
compare-and-set, setting the username to the ID of the user who claimed it, provided that the
username is not already taken.