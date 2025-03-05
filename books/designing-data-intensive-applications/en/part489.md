*  If you can’t use a serializable isolation level, the second-best option in this case is probably
to explicitly lock the rows that the transaction depends on. In the doctors example, you could
write something like the following: BEGIN TRANSACTION;

SELECT * FROM doctors
  WHERE on_call = true
  AND shift_id = 1234 FOR UPDATE; [![1](assets/1.png)](#callout_transactions_CO2-1)

UPDATE doctors
  SET on_call = false
  WHERE name = 'Alice'
  AND shift_id = 1234;

COMMIT; [![1](assets/1.png)](#co_transactions_CO2-1) As before, FOR UPDATE tells the database to lock all rows returned by this query. ### More examples of write skew 
Write skew may seem like an esoteric issue at first, but once you’re aware of it, you may notice
more situations in which it can occur. Here are some more examples: Meeting room booking system 
Say you want to enforce that there cannot be two bookings for the same meeting room at the same
time [[43](ch07.html#Terry1995dn_ch7)].
When someone wants to make a booking, you first check for any conflicting bookings (i.e.,
bookings for the same room with an overlapping time range), and if none are found, you create the
meeting (see
[Example 7-2](#fig_transactions_meeting_rooms)).[ix](ch07.html#idm140605761767776)