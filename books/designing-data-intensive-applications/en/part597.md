All of this requires a large amount of additional work and severely restricts the range of
programming languages, libraries, and tools that can be used (since most languages and tools do not
provide real-time guarantees). For these reasons, developing real-time systems is very expensive,
and they are most commonly used in safety-critical embedded devices. Moreover, “real-time” is not the
same as “high-performance”—in fact, real-time systems may have lower throughput, since they have to
prioritize timely responses above all else (see also [“Latency and Resource Utilization”](#sidebar_distributed_latency_utilization)). For most server-side data processing systems, real-time guarantees are simply not economical or
appropriate. Consequently, these systems must suffer the pauses and clock instability that come from
operating in a non-real-time environment. ### Limiting the impact of garbage collection The negative effects of process pauses can be mitigated without resorting to expensive real-time
scheduling guarantees. Language runtimes have some flexibility around when they schedule garbage
collections, because they can track the rate of object allocation and the remaining free memory over
time.