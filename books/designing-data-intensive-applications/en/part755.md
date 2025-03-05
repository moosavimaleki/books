It could still happen that a node is incorrectly declared dead by consensus, even though it is
actually alive. But it is nevertheless very useful for a system to have agreement on which nodes
constitute the current membership. For example, choosing a leader could mean simply choosing the
lowest-numbered among the current members, but this approach would not work if different nodes have
divergent opinions on who the current members are. # Summary In this chapter we examined the topics of consistency and consensus from several different angles.
We looked in depth at linearizability, a popular consistency model: its goal is to make replicated
data appear as though there were only a single copy, and to make all operations act on it atomically.
Although linearizability is appealing because it is easy to understand—it makes a database behave
like a variable in a single-threaded program—it has the downside of being slow, especially in
environments with large network delays.