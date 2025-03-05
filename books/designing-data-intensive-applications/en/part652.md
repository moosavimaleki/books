write(x, v) ⇒ r means the client requested to set the
register x to value v, and the database returned response r (which could be ok or error). In [Figure 9-2](#fig_consistency_linearizability_1), the value of x is initially 0, and client C performs a
write request to set it to 1. While this is happening, clients A and B are repeatedly polling the
database to read the latest value. What are the possible responses that A and B might get for their
read requests? *  
The first read operation by client A completes before the write begins, so it must definitely
return the old value 0. *  The last read by client A begins after the write has completed, so it must definitely return the
new value 1 if the database is linearizable: we know that the write must have been processed
sometime between the start and end of the write operation, and the read must have been processed
sometime between the start and end of the read operation. If the read started after the write
ended, then the read must have been processed after the write, and therefore it must see the new
value that was written.