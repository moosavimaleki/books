*  Any read operations that overlap in time with the write operation might return either 0 or 1,
because we don’t know whether or not the write has taken effect at the time when the read
operation is processed. These operations are concurrent with the write. However, that is not yet sufficient to fully describe linearizability: if reads that are concurrent
with a write can return either the old or the new value, then readers could see a value flip back
and forth between the old and the new value several times while a write is going on. That is not
what we expect of a system that emulates a “single copy of the
data.”[ii](ch09.html#idm140605760046160) To make the system linearizable, we need to add another constraint, illustrated in
[Figure 9-3](#fig_consistency_linearizability_2). ![ddia 0903](assets/ddia_0903.png) ###### Figure 9-3. After any one read has returned the new value, all following reads (on the same or other clients) must also return the new value.