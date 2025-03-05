The handling of output from MapReduce jobs follows the same philosophy. By treating inputs as
immutable and avoiding side effects (such as writing to external databases), batch jobs not only
achieve good performance but also become much easier to maintain: *  
If you introduce a bug into the code and the output is wrong or corrupted, you can simply roll
back to a previous version of the code and rerun the job, and the output will be correct again. Or,
even simpler, you can keep the old output in a different directory and simply switch back to it.
Databases with read-write transactions do not have this property: if you deploy buggy code that
writes bad data to the database, then rolling back the code will do nothing to fix the data in the
database. 
(The idea of being able to recover from buggy code has been called human fault tolerance
[[50](ch10.html#Marz2011vq)].)