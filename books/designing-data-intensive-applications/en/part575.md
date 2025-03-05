
NTP may adjust the frequency at which the monotonic clock moves forward (this is known as slewing
the clock) if it detects that the computer’s local quartz is moving faster or slower than the NTP
server. By default, NTP allows the clock rate to be speeded up or slowed down by up to 0.05%, but
NTP cannot cause the monotonic clock to jump forward or backward. The resolution of monotonic
clocks is usually quite good: on most systems they can measure time intervals in microseconds or
less. In a distributed system, using a monotonic clock for measuring elapsed time (e.g., timeouts) is
usually fine, because it doesn’t assume any synchronization between different nodes’ clocks and is
not sensitive to slight inaccuracies of measurement. ## Clock Synchronization and Accuracy 
Monotonic clocks don’t need synchronization, but time-of-day clocks need to be set according to an
NTP server or other external time source in order to be useful. Unfortunately, our methods for
getting a clock to tell the correct time aren’t nearly as reliable or accurate as you might
hope—hardware clocks and NTP can be fickle beasts. To give just a few examples: