
Similarly, in event sourcing, application state is maintained by applying a log of events; here the
application state is also a kind of materialized view. Unlike stream analytics scenarios, it is
usually not sufficient to consider only events within some time window: building the materialized
view potentially requires all events over an arbitrary time period, apart from any obsolete events
that may be discarded by log compaction (see [“Log compaction”](#sec_stream_log_compaction)). In effect, you need a
window that stretches all the way back to the beginning of time. 
In principle, any stream processor could be used for materialized view maintenance, although the
need to maintain events forever runs counter to the assumptions of some analytics-oriented
frameworks that mostly operate on windows of a limited duration. Samza and Kafka Streams support
this kind of usage, building upon Kafka’s support for log compaction
[[75](ch11.html#Kreps2014wm_ch11)]. ### Search on streams 
Besides CEP, which allows searching for patterns consisting of multiple events, there is also
sometimes a need to search for individual events based on complex criteria, such as full-text search
queries.