A 2PC transaction begins with the application reading and writing data on multiple database nodes,
as normal. We call these database nodes participants in the transaction. When the application is
ready to commit, the coordinator begins phase 1: it sends a prepare request to each of the nodes,
asking them whether they are able to commit. The coordinator then tracks the responses from the
participants: *  If all participants reply “yes,” indicating they are ready to commit, then the coordinator sends
out a commit request in phase 2, and the commit actually takes place. *  
If any of the participants replies “no,” the coordinator sends an abort request to all nodes in
phase 2. This process is somewhat like the traditional marriage ceremony in Western cultures: the minister
asks the bride and groom individually whether each wants to marry the other, and typically receives
the answer “I do” from both. After receiving both acknowledgments, the minister pronounces the
couple husband and wife: the transaction is committed, and the happy fact is broadcast to all
attendees. If either bride or groom does not say “yes,” the ceremony is aborted
[[73](ch09.html#Gray1981wi_ch9)].