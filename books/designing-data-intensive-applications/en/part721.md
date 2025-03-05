
If the coordinator fails before sending the prepare requests, a participant can safely abort the
transaction. But once the participant has received a prepare request and voted “yes,” it can no
longer abort unilaterally—it must wait to hear back from the coordinator whether the transaction
was committed or aborted. If the coordinator crashes or the network fails at this point, the
participant can do nothing but wait. A participant’s transaction in this state is called in doubt
or uncertain. The situation is illustrated in [Figure 9-10](#fig_consistency_2pc_crash). In this particular example, the
coordinator actually decided to commit, and database 2 received the commit request. However, the
coordinator crashed before it could send the commit request to database 1, and so database 1 does
not know whether to commit or abort. Even a timeout does not help here: if database 1 unilaterally
aborts after a timeout, it will end up inconsistent with database 2, which has committed. Similarly,
it is not safe to unilaterally commit, because another participant may have aborted.