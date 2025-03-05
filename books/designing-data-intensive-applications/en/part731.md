### Recovering from coordinator failure 
In theory, if the coordinator crashes and is restarted, it should cleanly recover its state from the
log and resolve any in-doubt transactions. However, in practice, orphaned in-doubt transactions do
occur [[89](ch09.html#Dhariwal2008vq),
[90](ch09.html#Randal2013wu)]—that is,
transactions for which the coordinator cannot decide the outcome for whatever reason (e.g., because
the transaction log has been lost or corrupted due to a software bug). These transactions cannot be
resolved automatically, so they sit forever in the database, holding locks and blocking other
transactions. Even rebooting your database servers will not fix this problem, since a correct implementation of
2PC must preserve the locks of an in-doubt transaction even across restarts (otherwise it would risk
violating the atomicity guarantee). It’s a sticky situation. The only way out is for an administrator to manually decide whether to commit or roll back the
transactions. The administrator must examine the participants of each in-doubt transaction,
determine whether any participant has committed or aborted already, and then apply the same outcome
to the other participants. Resolving the problem potentially requires a lot of manual effort, and
most likely needs to be done under high stress and time pressure during a serious production outage
(otherwise, why would the coordinator be in such a bad state?).