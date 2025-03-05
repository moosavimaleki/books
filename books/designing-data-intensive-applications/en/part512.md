
In the meeting room booking example this means that if one transaction has searched for existing
bookings for a room within a certain time window (see [Example 7-2](#fig_transactions_meeting_rooms)), another
transaction is not allowed to concurrently insert or update another booking for the same room and
time range. (It’s okay to concurrently insert bookings for other rooms, or for the same room at a
different time that doesn’t affect the proposed booking.) How do we implement this? Conceptually, we need a predicate lock
[[3](ch07.html#Eswaran1976uu)]. It works similarly to the
shared/exclusive lock described earlier, but rather than belonging to a particular object (e.g., one
row in a table), it belongs to all objects that match some search condition, such as: ```
`SELECT` `*` `FROM` `bookings`
  `WHERE` `room_id` `=` `123` `AND`
    `end_time`   `>` `'2018-01-01 12:00'` `AND`
    `start_time` `<` `'2018-01-01 13:00'``;`
``` A predicate lock restricts access as follows: *  If transaction A wants to read objects matching some condition, like in that SELECT query, it
must acquire a shared-mode predicate lock on the conditions of the query. If another transaction B
currently has an exclusive lock on any object matching those conditions, A must wait until B
releases its lock before it is allowed to make its query.