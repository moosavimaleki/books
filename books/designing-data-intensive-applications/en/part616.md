
With regard to timing assumptions, three system models are in common use: Synchronous model 
The synchronous model assumes bounded network delay, bounded process pauses, and bounded clock
error. This does not imply exactly synchronized clocks or zero network delay; it just means you
know that network delay, pauses, and clock drift will never exceed some fixed upper bound
[[88](ch08.html#Dwork1988dr_ch8)].
The synchronous model is not a realistic model of most practical
systems, because (as discussed in this chapter) unbounded delays and pauses do occur. Partially synchronous model Partial synchrony means that a system behaves like a synchronous system most of the time, but it
sometimes exceeds the bounds for network delay, process pauses, and clock drift
[[88](ch08.html#Dwork1988dr_ch8)]. This is a realistic model of many
systems: most of the time, networks and processes are quite well behaved—otherwise we would never
be able to get anything done—but we have to reckon with the fact that any timing assumptions
may be shattered occasionally. When this happens, network delay, pauses, and clock error may become
arbitrarily large.