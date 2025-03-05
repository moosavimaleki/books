A bug in the software could be regarded as a Byzantine fault, but if you deploy the same software to
all nodes, then a Byzantine fault-tolerant algorithm cannot save you. Most Byzantine fault-tolerant
algorithms require a supermajority of more than two-thirds of the nodes to be functioning correctly
(i.e., if you have four nodes, at most one may malfunction). To use this approach against bugs, you
would have to have four independent implementations of the same software and hope that a bug only
appears in one of the four implementations. 
Similarly, it would be appealing if a protocol could protect us from vulnerabilities, security
compromises, and malicious attacks. Unfortunately, this is not realistic either: in most systems, if
an attacker can compromise one node, they can probably compromise all of them, because they are
probably running the same software. Thus, traditional mechanisms (authentication, access control,
encryption, firewalls, and so on) continue to be the main protection against attackers.