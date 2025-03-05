##### Example 7-2. A meeting room booking system tries to avoid double-booking (not safe under snapshot isolation) ```
`BEGIN` `TRANSACTION``;`

`-- Check for any existing bookings that overlap with the period of noon-1pm`
`SELECT` `COUNT``(``*``)` `FROM` `bookings`
  `WHERE` `room_id` `=` `123` `AND`
    `end_time` `>` `'2015-01-01 12:00'` `AND` `start_time` `<` `'2015-01-01 13:00'``;`

`-- If the previous query returned zero:`
`INSERT` `INTO` `bookings`
  `(``room_id``,` `start_time``,` `end_time``,` `user_id``)`
  `VALUES` `(``123``,` `'2015-01-01 12:00'``,` `'2015-01-01 13:00'``,` `666``);`

`COMMIT``;`
``` Unfortunately, snapshot isolation does not prevent another user from concurrently inserting a conflicting
meeting. In order to guarantee you won’t get scheduling conflicts, you once again need serializable
isolation. Multiplayer game In [Example 7-1](#fig_transactions_select_for_update), we used a lock to prevent lost updates (that is, making
sure that two players can’t move the same figure at the same time). However, the lock doesn’t
prevent players from moving two different figures to the same position on the board or potentially
making some other move that violates the rules of the game. Depending on the kind of rule you are
enforcing, you might be able to use a unique constraint, but otherwise you’re vulnerable to write
skew.