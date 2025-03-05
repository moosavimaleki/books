```
`SELECT` `COUNT``(``*``)` `FROM` `emails` `WHERE` `recipient_id` `=` `2` `AND` `unread_flag` `=` `true`
``` 
However, you might find this query to be too slow if there are many emails, and decide to store the
number of unread messages in a separate field (a kind of denormalization). Now, whenever a new
message comes in, you have to increment the unread counter as well, and whenever a message is marked
as read, you also have to decrement the unread counter. 
In [Figure 7-2](#fig_transactions_read_uncommitted), user 2 experiences an anomaly: the mailbox listing shows
an unread message, but the counter shows zero unread messages because the counter increment has not
yet happened.[ii](ch07.html#idm140605774708544)
Isolation would have prevented this issue by ensuring that user 2 sees either both the inserted
email and the updated counter, or neither, but not an inconsistent halfway point. ![ddia 0702](assets/ddia_0702.png) ###### Figure 7-2. Violating isolation: one transaction reads another transaction’s uncommitted writes (a “dirty read”).