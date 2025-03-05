
Could NTP synchronization be made accurate enough that such incorrect orderings cannot occur?
Probably not, because NTP’s synchronization accuracy is itself limited by the network round-trip
time, in addition to other sources of error such as quartz drift. For correct ordering, you would
need the clock source to be significantly more accurate than the thing you are measuring (namely
network delay). 
So-called logical clocks
[[56](ch08.html#Lamport1978jq_ch8),
[57](ch08.html#Kulkarni2014ws)],
which are based on incrementing counters rather than an oscillating quartz crystal, are a safer
alternative for ordering events (see [“Detecting Concurrent Writes”](ch05.html#sec_replication_concurrent)). Logical clocks do not measure
the time of day or the number of seconds elapsed, only the relative ordering of events (whether one
event happened before or after another). In contrast, time-of-day and monotonic clocks, which
measure actual elapsed time, are also known as physical clocks. We’ll look at ordering a bit more
in [“Ordering Guarantees”](ch09.html#sec_consistency_ordering). ### Clock readings have a confidence interval