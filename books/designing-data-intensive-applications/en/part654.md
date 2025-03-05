In a linearizable system we imagine that there must be some point in time (between the start and end
of the write operation) at which the value of x atomically flips from 0 to 1. Thus, if one
client’s read returns the new value 1, all subsequent reads must also return the new value, even if
the write operation has not yet completed. This timing dependency is illustrated with an arrow in [Figure 9-3](#fig_consistency_linearizability_2).
Client A is the first to read the new value, 1. Just after A’s read returns, B begins a new read.
Since B’s read occurs strictly after A’s read, it must also return 1, even though the write by C is
still ongoing. (It’s the same situation as with Alice and Bob in
[Figure 9-1](#fig_consistency_linearizability_0): after Alice has read the new value, Bob also expects to read
the new value.) We can further refine this timing diagram to visualize each operation taking effect atomically at
some point in time. A more complex example is shown in [Figure 9-4](#fig_consistency_linearizability_3)
[[10](ch09.html#Kingsbury2015uh)].