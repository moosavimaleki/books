Representing databases as streams opens up powerful opportunities for integrating systems. You can
keep derived data systems such as search indexes, caches, and analytics systems continually
up to date by consuming the log of changes and applying them to the derived system. You can even
build fresh views onto existing data by starting from scratch and consuming the log of changes from
the beginning all the way to the present. The facilities for maintaining state as streams and replaying messages are also the basis for the
techniques that enable stream joins and fault tolerance in various stream processing frameworks.
We discussed several purposes of stream processing, including searching for event patterns (complex
event processing), computing windowed aggregations (stream analytics), and keeping derived data
systems up to date (materialized views). We then discussed the difficulties of reasoning about time in a stream processor, including the
distinction between processing time and event timestamps, and the problem of dealing with straggler
events that arrive after you thought your window was complete.