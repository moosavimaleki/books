*  
As a consequence of this ease of rolling back, feature development can proceed more quickly than
in an environment where mistakes could mean irreversible damage. This principle of minimizing
irreversibility is beneficial for Agile software development
[[51](ch10.html#Bartlett2015wv_ch10)]. *  
If a map or reduce task fails, the MapReduce framework automatically re-schedules it and runs it
again on the same input. If the failure is due to a bug in the code, it will keep crashing and
eventually cause the job to fail after a few attempts; but if the failure is due to a transient
issue, the fault is tolerated. This automatic retry is only safe because inputs are immutable and
outputs from failed tasks are discarded by the MapReduce framework. *  The same set of files can be used as input for various different jobs, including monitoring jobs
that calculate metrics and evaluate whether a job’s output has the expected characteristics (for
example, by comparing it to the output from the previous run and measuring discrepancies).