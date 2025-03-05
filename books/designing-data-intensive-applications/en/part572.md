
Moreover, each machine on the network has its own clock, which is an actual hardware device: usually
a quartz crystal oscillator. These devices are not perfectly accurate, so each machine has its own
notion of time, which may be slightly faster or slower than on other machines. It is possible to
synchronize clocks to some degree: the most commonly used mechanism is the Network Time Protocol (NTP), which
allows the computer clock to be adjusted according to the time reported by a group of servers
[[37](ch08.html#Windl2006uo)]. The servers in turn get their time from a more accurate time source, such
as a GPS receiver. ## Monotonic Versus Time-of-Day Clocks 
Modern computers have at least two different kinds of clocks: a time-of-day clock and a monotonic
clock. Although they both measure time, it is important to distinguish the two, since they serve
different purposes. ### Time-of-day clocks 
A time-of-day clock does what you intuitively expect of a clock: it returns the current date and
time according to some calendar (also known as wall-clock time). For example,
clock_gettime(CLOCK_REALTIME) on Linux[v](ch08.html#idm140605760841440) and
System.currentTimeMillis() in Java return the number of seconds (or milliseconds) since the
epoch: midnight UTC on January 1, 1970, according to the Gregorian calendar, not counting leap
seconds. Some systems use other dates as their reference point.