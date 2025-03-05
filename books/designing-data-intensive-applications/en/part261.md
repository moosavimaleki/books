*  Via databases (see [“Dataflow Through Databases”](#sec_encoding_dataflow_db)) *  Via service calls (see [“Dataflow Through Services: REST and RPC”](#sec_encoding_dataflow_rpc)) *  Via asynchronous message passing (see [“Message-Passing Dataflow”](#sec_encoding_dataflow_msg)) ## Dataflow Through Databases 
In a database, the process that writes to the database encodes the data, and the process that reads
from the database decodes it. There may just be a single process accessing the database, in which
case the reader is simply a later version of the same process—in that case you can think of
storing something in the database as sending a message to your future self. Backward compatibility is clearly necessary here; otherwise your future self won’t be able to decode
what you previously wrote. In general, it’s common for several different processes to be accessing a database at the same time.
Those processes might be several different applications or services, or they may simply be several
instances of the same service (running in parallel for scalability or fault tolerance). Either way,
in an environment where the application is changing, it is likely that some processes accessing the
database will be running newer code and some will be running older code—for example because a new
version is currently being deployed in a rolling upgrade, so some instances have been updated while
others haven’t yet.