*  Alternatively, if the database uses a time-based index to find existing bookings, it can attach a
shared lock to a range of values in that index, indicating that a transaction has searched for
bookings that overlap with the time period of noon to 1 p.m. on January 1, 2018. Either way, an approximation of the search condition is attached to one of the indexes. Now, if
another transaction wants to insert, update, or delete a booking for the same room and/or an
overlapping time period, it will have to update the same part of the index. In the process of doing
so, it will encounter the shared lock, and it will be forced to wait until the lock is released. This provides effective protection against phantoms and write skew. Index-range locks are not as
precise as predicate locks would be (they may lock a bigger range of objects than is strictly
necessary to maintain serializability), but since they have much lower overheads, they are a good
compromise.