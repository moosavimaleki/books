
You can implement such a linearizable compare-and-set operation as follows by using total order
broadcast as an append-only log
[[62](ch09.html#Balakrishnan2013ko),
[63](ch09.html#vanRenesse2004td)]: 1.  Append a message to the log, tentatively indicating the username you want to claim. 2.  Read the log, and wait for the message you appended to be delivered back to
you.[xi](ch09.html#idm140605759417392) 3.  Check for any messages claiming the username that you want. If the first message for your desired
username is your own message, then you are successful: you can commit the username claim (perhaps
by appending another message to the log) and acknowledge it to the client. If the first message
for your desired username is from another user, you abort the operation. 
Because log entries are delivered to all nodes in the same order, if there are several concurrent
writes, all nodes will agree on which one came first. Choosing the first of the conflicting
writes as the winner and aborting later ones ensures that all nodes agree on whether a write was
committed or aborted.  A similar approach can be used to implement serializable multi-object
transactions on top of a log [[62](ch09.html#Balakrishnan2013ko)].