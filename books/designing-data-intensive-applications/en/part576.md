*  
The quartz clock in a computer is not very accurate: it drifts (runs faster or slower than it
should). Clock drift varies depending on the temperature of the machine. Google assumes a clock
drift of 200 ppm (parts per million) for its servers
[[41](ch08.html#Corbett2012uz_ch8)],
which is equivalent to 6 ms drift for a clock that is resynchronized with a server every 30
seconds, or 17 seconds drift for a clock that is resynchronized once a day. This drift limits the best
possible accuracy you can achieve, even if everything is working correctly. *  If a computer’s clock differs too much from an NTP server, it may refuse to synchronize, or the
local clock will be forcibly reset [[37](ch08.html#Windl2006uo)]. Any
applications observing the time before and after this reset may see time go backward or suddenly
jump forward. *  If a node is accidentally firewalled off from NTP servers, the misconfiguration may go
unnoticed for some time. Anecdotal evidence suggests that this does happen in practice.