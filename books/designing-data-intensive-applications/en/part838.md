These databases need to be queried from the web application that handles user requests, which is
usually separate from the Hadoop infrastructure. So how does the output from the batch process get
back into a database where the web application can query it? 
The most obvious choice might be to use the client library for your favorite database directly
within a mapper or reducer, and to write from the batch job directly to the database server, one
record at a time. This will work (assuming your firewall rules allow direct access from your Hadoop
environment to your production databases), but it is a bad idea for several reasons: *  As discussed previously in the context of joins, making a network request for every single record
is orders of magnitude slower than the normal throughput of a batch task. Even if the client
library supports batching, performance is likely to be poor.