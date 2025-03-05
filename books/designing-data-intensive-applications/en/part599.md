These measures cannot fully prevent garbage collection pauses, but they can usefully reduce their
impact on the application. # Knowledge, Truth, and Lies So far in this chapter we have explored the ways in which distributed systems are different from
programs running on a single computer: there is no shared memory, only message passing via an
unreliable network with variable delays, and the systems may suffer from partial failures, unreliable clocks,
and processing pauses. The consequences of these issues are profoundly disorienting if you’re not used to distributed
systems. A node in the network cannot know anything for sure—it can only make guesses based on
the messages it receives (or doesn’t receive) via the network. A node can only find out what state
another node is in (what data it has stored, whether it is correctly functioning, etc.) by
exchanging messages with it. If a remote node doesn’t respond, there is no way of knowing what state
it is in, because problems in the network cannot reliably be distinguished from problems at a node.