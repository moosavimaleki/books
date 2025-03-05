
Implementations of CEP include Esper
[[69](ch11.html#Esper2016)],
IBM InfoSphere Streams
[[70](ch11.html#Nabi2014wu)],
Apama, TIBCO StreamBase, and SQLstream. Distributed stream processors like Samza are also gaining
SQL support for declarative queries on streams
[[71](ch11.html#Pathirage2016fr)]. ### Stream analytics 
Another area in which stream processing is used is for analytics on streams. The boundary between
CEP and stream analytics is blurry, but as a general rule, analytics tends to be less interested in
finding specific event sequences and is more oriented toward aggregations and statistical metrics
over a large number of events—for example: *  Measuring the rate of some type of event (how often it occurs per time interval) *  Calculating the rolling average of a value over some time period *  Comparing current statistics to previous time intervals (e.g., to detect trends or to alert on
metrics that are unusually high or low compared to the same time last week) 
Such statistics are usually computed over fixed time intervals—for example, you might want to
know the average number of queries per second to a service over the last 5 minutes, and their
99th percentile response time during that period. Averaging over a few minutes smoothes out
irrelevant fluctuations from one second to the next, while still giving you a timely picture of any
changes in traffic pattern. The time interval over which you aggregate is known as a window, and
we will look into windowing in more detail in [“Reasoning About Time”](#sec_stream_time).