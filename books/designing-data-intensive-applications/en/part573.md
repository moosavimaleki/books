
Time-of-day clocks are usually synchronized with NTP, which means that a timestamp from one machine
(ideally) means the same as a timestamp on another machine. However, time-of-day clocks also have
various oddities, as described in the next section. In particular, if the local clock is too far
ahead of the NTP server, it may be forcibly reset and appear to jump back to a previous point in
time. These jumps, as well as the fact that they often ignore leap seconds, make time-of-day clocks
unsuitable for measuring elapsed time
[[38](ch08.html#GrahamCumming2017db)]. Time-of-day clocks have also historically had quite a coarse-grained resolution, e.g., moving forward
in steps of 10 ms on older Windows systems
[[39](ch08.html#Holmes2006uj)]. On recent systems, this is less of a problem. ### Monotonic clocks 
A monotonic clock is suitable for measuring a duration (time interval), such as a timeout or a
service’s response time: clock_gettime(CLOCK_MONOTONIC) on Linux and
System.nanoTime() in Java are monotonic clocks, for example. The name comes from the fact that they are
guaranteed to always move forward (whereas a time-of-day clock may jump back in time).