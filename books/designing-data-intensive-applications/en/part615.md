*  
  NTP clients can be configured with multiple server addresses. When synchronizing, the client
  contacts all of them, estimates their errors, and checks that a majority of servers agree on some
  time range. As long as most of the servers are okay, a misconfigured NTP server that is reporting an
  incorrect time is detected as an outlier and is excluded from synchronization
  [[37](ch08.html#Windl2006uo)]. The use of multiple servers makes NTP
  more robust than if it only uses a single server. ## System Model and Reality 
Many algorithms have been designed to solve distributed systems problems—for example, we will
examine solutions for the consensus problem in [Chapter 9](ch09.html#ch_consistency). In order to be useful, these
algorithms need to tolerate the various faults of distributed systems that we discussed in this
chapter. Algorithms need to be written in a way that does not depend too heavily on the details of the
hardware and software configuration on which they are run. This in turn requires that we somehow
formalize the kinds of faults that we expect to happen in a system. We do this by defining a system
model, which is an abstraction that describes what things an algorithm may assume.