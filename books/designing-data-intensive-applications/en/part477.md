As a result, nobody really knows what repeatable read means. ## Preventing Lost Updates 
The read committed and snapshot isolation levels we’ve discussed so far have been primarily about the guarantees
of what a read-only transaction can see in the presence of concurrent writes. We have mostly ignored
the issue of two transactions writing concurrently—we have only discussed dirty writes (see
[“No dirty writes”](#sec_transactions_dirty_write)), one particular type of write-write conflict that can occur. 
There are several other interesting kinds of conflicts that can occur between concurrently writing
transactions. The best known of these is the lost update problem, illustrated in
[Figure 7-1](#fig_transactions_increment) with the example of two concurrent counter increments. 
The lost update problem can occur if an application reads some value from the database, modifies it,
and writes back the modified value (a read-modify-write cycle). If two transactions do this
concurrently, one of the modifications can be lost, because the second write does not include the
first modification. (We sometimes say that the later write clobbers the earlier write.) This
pattern occurs in various different scenarios: