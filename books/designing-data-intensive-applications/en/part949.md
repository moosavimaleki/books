
Storing data is normally quite straightforward if you don’t have to worry about how it is going to
be queried and accessed; many of the complexities of schema design, indexing, and storage engines
are the result of wanting to support certain query and access patterns (see [Chapter 3](ch03.html#ch_storage)). For
this reason, you gain a lot of flexibility by separating the form in which data is written from the
form it is read, and by allowing several different read views. This idea is sometimes known as
command query responsibility segregation (CQRS) [[42](ch11.html#Young2014wp),
[58](ch11.html#Fowler2011xt),
[59](ch11.html#Young2010td)]. 
The traditional approach to database and schema design is based on the fallacy that data must be
written in the same form as it will be queried. Debates about normalization and denormalization (see
[“Many-to-One and Many-to-Many Relationships”](ch02.html#sec_datamodels_many_to_many)) become largely irrelevant if you can translate data from a
write-optimized event log to read-optimized application state: it is entirely reasonable to
denormalize data in the read-optimized views, as the translation process gives you a mechanism for
keeping it consistent with the event log.