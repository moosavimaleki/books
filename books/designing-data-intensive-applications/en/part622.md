
Safety and liveness properties and system models are very useful for reasoning about the correctness
of a distributed algorithm. However, when implementing an algorithm in practice, the messy facts of
reality come back to bite you again, and it becomes clear that the system model is a simplified
abstraction of reality. 
For example, algorithms in the crash-recovery model generally assume that data in stable storage
survives crashes. However, what happens if the data on disk is corrupted, or the data is wiped out
due to hardware error or misconfiguration
[[91](ch08.html#Junqueira2015wf)]? What happens if a server has a firmware bug and fails to recognize
its hard drives on reboot, even though the drives are correctly attached to the server
[[92](ch08.html#Sanders2016tl)]? 
Quorum algorithms (see [“Quorums for reading and writing”](ch05.html#sec_replication_quorum_condition)) rely on a node remembering the data
that it claims to have stored. If a node may suffer from amnesia and forget previously stored data,
that breaks the quorum condition, and thus breaks the correctness of the algorithm. Perhaps a new
system model is needed, in which we assume that stable storage mostly survives crashes, but may
sometimes be lost. But that model then becomes harder to reason about.