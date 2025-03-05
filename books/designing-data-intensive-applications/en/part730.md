The database cannot release those locks until the transaction commits or aborts (illustrated as a
shaded area in [Figure 9-9](#fig_consistency_two_phase_commit)). Therefore, when using two-phase commit, a
transaction must hold onto the locks throughout the time it is in doubt. If the coordinator has
crashed and takes 20 minutes to start up again, those locks will be held for 20 minutes. If the
coordinator’s log is entirely lost for some reason, those locks will be held forever—or at least
until the situation is manually resolved by an administrator. While those locks are held, no other transaction can modify those rows. Depending on the database,
other transactions may even be blocked from reading those rows. Thus, other transactions cannot
simply continue with their business—if they want to access that same data, they will be blocked.
This can cause large parts of your application to become unavailable until the in-doubt transaction
is resolved.