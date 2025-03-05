The reduce-side approach has the advantage that you do not need to make any assumptions about the
input data: whatever its properties and structure, the mappers can prepare the data to be ready for
joining. However, the downside is that all that sorting, copying to reducers, and merging of reducer
inputs can be quite expensive. Depending on the available memory buffers, data may be written to
disk several times as it passes through the stages of MapReduce
[[37](ch10.html#Grover2015tl)]. On the other hand, if you can make certain assumptions about your input data, it is possible to
make joins faster by using a so-called map-side join. This approach uses a cut-down MapReduce job
in which there are no reducers and no sorting. Instead, each mapper simply reads one input file
block from the distributed filesystem and writes one output file to the filesystem—that is all. ### Broadcast hash joins 
The simplest way of performing a map-side join applies in the case where a large dataset is joined
with a small dataset. In particular, the small dataset needs to be small enough that it can be
loaded entirely into memory in each of the mappers.