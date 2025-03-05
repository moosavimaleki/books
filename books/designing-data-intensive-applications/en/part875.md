These dataflow APIs generally use relational-style building blocks to express a computation: joining
datasets on the value of some field; grouping tuples by key; filtering by some condition; and
aggregating tuples by counting, summing, or other functions. Internally, these operations are
implemented using the various join and grouping algorithms that we discussed earlier in this
chapter. Besides the obvious advantage of requiring less code, these high-level interfaces also allow
interactive use, in which you write analysis code incrementally in a shell and run it frequently to
observe what it is doing. This style of development is very helpful when exploring a dataset and
experimenting with approaches for processing it. It is also reminiscent of the Unix philosophy,
which we discussed in [“The Unix Philosophy”](#sec_batch_unix_philosophy). Moreover, these high-level interfaces not only make the humans using the system more productive, but
they also improve the job execution efficiency at a machine level.