# Part II. Distributed Data

# Part II. Distributed Data For a successful technology, reality must take precedence over public relations, for
        nature cannot be fooled. Richard Feynman, Rogers Commission Report (1986) In [Part I](part01.html#part_foundations) of this book, we discussed aspects of data
systems that apply when data is stored on a single machine. Now, in
[Part II](#part_distributed_data), we move up a level and ask: what happens if
multiple machines are involved in storage and retrieval of data? 
There are various reasons why you might want to distribute a database across multiple machines: Scalability If your data volume, read load, or write load grows bigger than a single machine can handle,
    you can potentially spread the load across multiple machines. Fault tolerance/high availability If your application needs to continue working even if one machine (or several machines, or
    the network, or an entire datacenter) goes down, you can use multiple machines to give you
    redundancy.  When one fails, another one can take over.