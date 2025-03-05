
In batch processing, a file is written once and then potentially read by multiple jobs. Analogously,
in streaming terminology, an event is generated once by a producer (also known as a publisher or
sender), and then potentially processed by multiple consumers (subscribers or recipients)
[[3](ch11.html#Eugster2003ih_ch11)].
In a filesystem, a filename identifies a set of related records; in a streaming system, related
events are usually grouped together into a topic or stream. In principle, a file or database is sufficient to connect producers and consumers: a producer writes
every event that it generates to the datastore, and each consumer periodically polls the datastore
to check for events that have appeared since it last ran. This is essentially what a batch process
does when it processes a day’s worth of data at the end of every day. However, when moving toward continual processing with low delays, polling becomes expensive if the
datastore is not designed for this kind of usage. The more often you poll, the lower the percentage
of requests that return new events, and thus the higher the overheads become. Instead, it is better
for consumers to be notified when new events appear.