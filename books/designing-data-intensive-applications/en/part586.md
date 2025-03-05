
The uncertainty bound can be calculated based on your time source. If you have a GPS receiver or
atomic (caesium) clock directly attached to your computer, the expected error range is reported by
the manufacturer. If you’re getting the time from a server, the uncertainty is based on the expected
quartz drift since your last sync with the server, plus the NTP server’s uncertainty, plus the
network round-trip time to the server (to a first approximation, and assuming you trust the server). Unfortunately, most systems don’t expose this uncertainty: for example, when you call
clock_gettime(), the return value doesn’t tell you the expected error of the timestamp, so you
don’t know if its confidence interval is five milliseconds or five years. 
An interesting exception is Google’s TrueTime API in Spanner
[[41](ch08.html#Corbett2012uz_ch8)], which explicitly reports the
confidence interval on the local clock. When you ask it for the current time, you get back two
values: [earliest, latest], which are the earliest possible and the latest possible
timestamp. Based on its uncertainty calculations, the clock knows that the actual current time is
somewhere within that interval. The width of the interval depends, among other things, on how long
it has been since the local quartz clock was last synchronized with a more accurate clock source.