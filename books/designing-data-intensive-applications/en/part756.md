We also explored causality, which imposes an ordering on events in a system (what happened before
what, based on cause and effect). Unlike linearizability, which puts all operations in a single,
totally ordered timeline, causality provides us with a weaker consistency model: some things can be
concurrent, so the version history is like a timeline with branching and merging. Causal consistency
does not have the coordination overhead of linearizability and is much less sensitive to network
problems. However, even if we capture the causal ordering (for example using Lamport timestamps), we saw that
some things cannot be implemented this way: in [“Timestamp ordering is not sufficient”](#sec_consistency_unique_constraint) we considered
the example of ensuring that a username is unique and rejecting concurrent registrations for the
same username. If one node is going to accept a registration, it needs to somehow know that another
node isn’t concurrently in the process of registering the same name. This problem led us toward
consensus.