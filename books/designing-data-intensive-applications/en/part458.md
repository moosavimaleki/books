*  If the transaction actually succeeded, but the network failed while the server tried to
acknowledge the successful commit to the client (so the client thinks it failed), then retrying
the transaction causes it to be performed twice—unless you have an additional application-level
deduplication mechanism in place. *  If the error is due to overload, retrying the transaction will make the problem worse, not better.
To avoid such feedback cycles, you can limit the number of retries, use exponential backoff, and
handle overload-related errors differently from other errors (if possible). *  It is only worth retrying after transient errors (for example due to deadlock, isolation
violation, temporary network interruptions, and failover); after a permanent error (e.g.,
constraint violation) a retry would be pointless. *  If the transaction also has side effects outside of the database, those side effects may happen
even if the transaction is aborted. For example, if you’re sending an email, you wouldn’t want to
send the email again every time you retry the transaction. If you want to make sure that several
different systems either commit or abort together, two-phase commit can help (we will discuss this
in [“Atomic Commit and Two-Phase Commit (2PC)”](ch09.html#sec_consistency_2pc)).