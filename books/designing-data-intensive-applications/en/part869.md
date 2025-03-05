
It is possible to store a graph in a distributed filesystem (in files containing lists of vertices
and edges), but this idea of “repeating until done” cannot be expressed in plain MapReduce, since it
only performs a single pass over the data. This kind of algorithm is thus often implemented in an
iterative style: 1.  An external scheduler runs a batch process to calculate one step of the algorithm. 2.  When the batch process completes, the scheduler checks whether it has finished (based on the
completion condition—e.g., there are no more edges to follow, or the change compared to the last
iteration is below some threshold). 3.  If it has not yet finished, the scheduler goes back to step 1 and runs another round of the batch
process. This approach works, but implementing it with MapReduce is often very inefficient, because MapReduce
does not account for the iterative nature of the algorithm: it will always read the entire input
dataset and produce a completely new output dataset, even if only a small part of the graph has
changed compared to the last iteration.