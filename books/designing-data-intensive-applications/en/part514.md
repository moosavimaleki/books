It’s safe to simplify a predicate by making it match a greater set of objects. For example, if you
have a predicate lock for bookings of room 123 between noon and 1 p.m., you can approximate it by
locking bookings for room 123 at any time, or you can approximate it by locking all rooms (not just
room 123) between noon and 1 p.m. This is safe, because any write that matches the original predicate
will definitely also match the approximations. In the room bookings database you would probably have an index on the room_id column, and/or
indexes on start_time and end_time (otherwise the preceding query would be very slow on a large
database): *  Say your index is on room_id, and the database uses this index to find existing bookings for
room 123. Now the database can simply attach a shared lock to this index entry, indicating that a
transaction has searched for bookings of room 123.