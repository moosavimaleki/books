Client B’s read returned 1 before client A received its response from the database, saying that
the write of the value 1 was successful. This is also okay: it doesn’t mean the value was read
before it was written, it just means the ok response from the database to client A was slightly
delayed in the network. *  This model doesn’t assume any transaction isolation: another client may change a value at any
time. For example, C first reads 1 and then reads 2, because the value was changed by B between
the two reads. An atomic compare-and-set (cas) operation can be used to check the value hasn’t
been concurrently changed by another client: B and C’s cas requests succeed, but D’s cas
request fails (by the time the database processes it, the value of x is no longer 0). *  The final read by client B (in a shaded bar) is not linearizable. The operation is concurrent with
C’s cas write, which updates x from 2 to 4. In the absence of other requests, it would be okay for
B’s read to return 2. However, client A has already read the new value 4 before B’s read started,
so B is not allowed to read an older value than A. Again, it’s the same situation as with Alice
and Bob in [Figure 9-1](#fig_consistency_linearizability_0).