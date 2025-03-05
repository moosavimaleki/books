A sorting operation inevitably needs to consume its entire input before it can produce any output,
because it’s possible that the very last input record is the one with the lowest key and thus needs
to be the very first output record. Any operator that requires sorting will thus need to accumulate
state, at least temporarily. But many other parts of a workflow can be executed in a pipelined
manner. When the job completes, its output needs to go somewhere durable so that users can find it and use
it—most likely, it is written to the distributed filesystem again. Thus, when using a dataflow
engine, materialized datasets on HDFS are still usually the inputs and the final outputs of a job.
Like with MapReduce, the inputs are immutable and the output is completely replaced. The improvement
over MapReduce is that you save yourself writing all the intermediate state to the filesystem as
well.