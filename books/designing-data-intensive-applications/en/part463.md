There are a few reasons why it’s useful to prevent dirty reads: *  If a transaction needs to update several objects, a dirty read means that another transaction may
see some of the updates but not others. For example, in [Figure 7-2](#fig_transactions_read_uncommitted), the
user sees the new unread email but not the updated counter. This is a dirty read of the email.
Seeing the database in a partially updated state is confusing to users and may cause other
transactions to take incorrect decisions. *  If a transaction aborts, any writes it has made need to be rolled back (like in
[Figure 7-3](#fig_transactions_atomicity)). If the database allows dirty reads, that means a transaction may
see data that is later rolled back—i.e., which is never actually committed to the database.
Reasoning about the consequences quickly becomes mind-bending. ### No dirty writes 
What happens if two transactions concurrently try to update the same object in a database? We don’t
know in which order the writes will happen, but we normally assume that the later write overwrites
the earlier write.