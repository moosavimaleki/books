
The distinguishing feature of a batch processing job is that it reads some input data and produces
some output data, without modifying the input—in other words, the output is derived from the
input. Crucially, the input data is bounded: it has a known, fixed size (for example, it
consists of a set of log files at some point in time, or a snapshot of a database’s contents).
Because it is bounded, a job knows when it has finished reading the entire input, and so a job
eventually completes when it is done. In the next chapter, we will turn to stream processing, in which the input is unbounded—that
is, you still have a job, but its inputs are never-ending streams of data. In this case, a job is
never complete, because at any time there may still be more work coming in. We shall see that stream
and batch processing are similar in some respects, but the assumption of unbounded streams also changes
a lot about how we build systems.