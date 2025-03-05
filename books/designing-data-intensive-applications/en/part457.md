Not all systems follow that philosophy, though. In particular, datastores with leaderless
replication (see [“Leaderless Replication”](ch05.html#sec_replication_leaderless)) work much more on a “best effort” basis, which
could be summarized as “the database will do as much as it can, and if it runs into an error, it
won’t undo something it has already done”—so it’s the application’s responsibility to recover from
errors. 
Errors will inevitably happen, but many software developers prefer to think only about the happy
path rather than the intricacies of error handling. For example, popular object-relational mapping
(ORM) frameworks such as Rails’s ActiveRecord and Django don’t retry aborted transactions—the
error usually results in an exception bubbling up the stack, so any user input is thrown away and
the user gets an error message. This is a shame, because the whole point of aborts is to enable safe
retries. Although retrying an aborted transaction is a simple and effective error handling mechanism, it
isn’t perfect: