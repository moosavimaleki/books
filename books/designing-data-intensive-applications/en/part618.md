Byzantine (arbitrary) faults 
Nodes may do absolutely anything, including trying to trick and deceive other nodes, as described
in the last section. For modeling real systems, the partially synchronous model with crash-recovery faults is generally
the most useful model. But how do distributed algorithms cope with that model? ### Correctness of an algorithm 
To define what it means for an algorithm to be correct, we can describe its properties. For
example, the output of a sorting algorithm has the property that for any two distinct elements of
the output list, the element further to the left is smaller than the element further to the right.
That is simply a formal way of defining what it means for a list to be sorted. 
Similarly, we can write down the properties we want of a distributed algorithm to define what it
means to be correct. For example, if we are generating fencing tokens for a lock (see
[“Fencing tokens”](#sec_distributed_fencing_tokens)), we may require the algorithm to have the following properties: