Proving an algorithm correct does not mean its implementation on a real system will necessarily
always behave correctly. But it’s a very good first step, because the theoretical analysis can
uncover problems in an algorithm that might remain hidden for a long time in a real system, and that
only come to bite you when your assumptions (e.g., about timing) are defeated due to unusual
circumstances. Theoretical analysis and empirical testing are equally important. # Summary In this chapter we have discussed a wide range of problems that can occur in distributed systems,
including: *  Whenever you try to send a packet over the network, it may be lost or arbitrarily delayed.
Likewise, the reply may be lost or delayed, so if you don’t get a reply, you have no idea whether
the message got through. *  A node’s clock may be significantly out of sync with other nodes (despite your best efforts to set
up NTP), it may suddenly jump forward or back in time, and relying on it is dangerous because you
most likely don’t have a good measure of your clock’s error interval.