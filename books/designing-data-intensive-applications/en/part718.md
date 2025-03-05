When the application is ready to commit, the coordinator sends a prepare request to all
participants, tagged with the global transaction ID. If any of these requests fails or times out,
the coordinator sends an abort request for that transaction ID to all participants. 4.  When a participant receives the prepare request, it makes sure that it can definitely commit
the transaction under all circumstances. 
This includes writing all transaction data to disk (a crash, a power failure, or running out of
disk space is not an acceptable excuse for refusing to commit later), and checking for any
conflicts or constraint violations. By replying “yes” to the coordinator, the node promises to
commit the transaction without error if requested. In other words, the participant surrenders the
right to abort the transaction, but without actually committing it. 5.  When the coordinator has received responses to all prepare requests, it makes a definitive
decision on whether to commit or abort the transaction (committing only if all participants voted
“yes”). The coordinator must write that decision to its transaction log on disk so that it knows
which way it decided in case it subsequently crashes. This is called the commit point.