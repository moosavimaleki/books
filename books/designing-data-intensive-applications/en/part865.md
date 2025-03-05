
In order to avoid such cascading faults, it is better to make operators deterministic. Note however
that it is easy for nondeterministic behavior to accidentally creep in: for example, many
programming languages do not guarantee any particular order when iterating over elements of a hash
table, many probabilistic and statistical algorithms
explicitly rely on using random numbers, and any use of the system clock or external data sources is
nondeterministic. Such causes of nondeterminism need to be removed in order to reliably recover from
faults, for example by generating pseudorandom numbers
using a fixed seed. Recovering from faults by recomputing data is not always the right answer: if the intermediate data
is much smaller than the source data, or if the computation is very CPU-intensive, it is probably
cheaper to materialize the intermediate data to files than to recompute it. ### Discussion of materialization 
Returning to the Unix analogy, we saw that MapReduce is like writing the output of each command to a
temporary file, whereas dataflow engines look much more like Unix pipes. Flink especially is built
around the idea of pipelined execution: that is, incrementally passing the output of an operator to
other operators, and not waiting for the input to be complete before starting to process it.