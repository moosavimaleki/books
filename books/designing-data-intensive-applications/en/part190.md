Besides performance, another interesting area for in-memory databases is providing data models that
are difficult to implement with disk-based indexes. For example, Redis offers a database-like
interface to various data structures such as priority queues and sets. Because it keeps all data in
memory, its implementation is comparatively simple. 
Recent research indicates that an in-memory database architecture could be extended to support
datasets larger than the available memory, without bringing back the overheads of a disk-centric architecture
[[45](ch03.html#DeBrabant2013ts)].
The so-called anti-caching approach works by evicting the least recently used data from memory to
disk when there is not enough memory, and loading it back into memory when it is accessed again in
the future. This is similar to what operating systems do with virtual memory and swap files, but the
database can manage memory more efficiently than the OS, as it can work at the granularity of
individual records rather than entire memory pages. This approach still requires indexes to fit
entirely in memory, though (like the Bitcask example at the beginning of the chapter).