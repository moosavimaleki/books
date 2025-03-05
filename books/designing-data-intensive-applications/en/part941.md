### Commands and events 
The event sourcing philosophy is careful to distinguish between events and commands
[[48](ch11.html#Mak2014ta)]. When a request from a
user first arrives, it is initially a command: at this point it may still fail, for example because
some integrity condition is violated. The application must first validate that it can execute the
command. If the validation is successful and the command is accepted, it becomes an event, which is
durable and immutable. For example, if a user tries to register a particular username, or reserve a seat on an airplane or
in a theater, then the application needs to check that the username or seat is not already taken.
(We previously discussed this example in [“Fault-Tolerant Consensus”](ch09.html#sec_consistency_consensus_ft).) When that check has
succeeded, the application can generate an event to indicate that a particular username was
registered by a particular user ID, or that a particular seat has been reserved for a particular
customer.