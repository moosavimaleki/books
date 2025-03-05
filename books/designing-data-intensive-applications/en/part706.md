Note that unlike Lamport timestamps, the numbers you get from incrementing the linearizable register
form a sequence with no gaps. Thus, if a node has delivered message 4 and receives an incoming
message with a sequence number of 6, it knows that it must wait for message 5 before it can deliver
message 6. The same is not the case with Lamport timestamps—in fact, this is the key difference
between total order broadcast and timestamp ordering. How hard could it be to make a linearizable integer with an atomic increment-and-get operation? As
usual, if things never failed, it would be easy: you could just keep it in a variable on one node.
The problem lies in handling the situation when network connections to that node are interrupted,
and restoring the value when that node fails
[[59](ch09.html#Balakrishnan2012wm)].
In general, if you think hard enough about linearizable sequence number generators, you inevitably
end up with a consensus algorithm.