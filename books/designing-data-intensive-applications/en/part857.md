
This setup is reasonable if the output from the first job is a dataset that you want to publish
widely within your organization. In that case, you need to be able to refer to it by name and reuse
it as input to several different jobs (including jobs developed by other teams). Publishing data to
a well-known location in the distributed filesystem allows loose coupling so that jobs don’t need
to know who is producing their input or consuming their output (see [“Separation of logic and wiring”](#sec_batch_logic_wiring)). 
However, in many cases, you know that the output of one job is only ever used as input to one other
job, which is maintained by the same team. In this case, the files on the distributed filesystem are
simply intermediate state: a means of passing data from one job to the next. In the complex
workflows used to build recommendation systems consisting of 50 or 100 MapReduce jobs
[[29](ch10.html#Sumbaly2013eh)], there is a lot of such intermediate
state.