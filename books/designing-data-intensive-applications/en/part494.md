### Materializing conflicts 
If the problem of phantoms is that there is no object to which we can attach the locks, perhaps we
can artificially introduce a lock object into the database? For example, in the meeting room booking case you could imagine creating a table of time slots and
rooms. Each row in this table corresponds to a particular room for a particular time period (say, 15
minutes). You create rows for all possible combinations of rooms and time periods ahead of time,
e.g. for the next six months. Now a transaction that wants to create a booking can lock (SELECT FOR UPDATE) the rows in the
table that correspond to the desired room and time period. After it has acquired the locks, it can
check for overlapping bookings and insert a new booking as before. Note that the additional table
isn’t used to store information about the booking—it’s purely a collection of locks which is used
to prevent bookings on the same room and time range from being modified concurrently.