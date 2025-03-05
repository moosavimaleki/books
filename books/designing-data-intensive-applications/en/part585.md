
You may be able to read a machine’s time-of-day clock with microsecond or even nanosecond
resolution. But even if you can get such a fine-grained measurement, that doesn’t mean the value is
actually accurate to such precision. In fact, it most likely is not—as mentioned previously, the
drift in an imprecise quartz clock can easily be several milliseconds, even if you synchronize with
an NTP server on the local network every minute. With an NTP server on the public internet, the best
possible accuracy is probably to the tens of milliseconds, and the error may easily spike to over
100 ms when there is network congestion [[57](ch08.html#Kulkarni2014ws)]. Thus, it doesn’t make sense to think of a clock reading as a point in time—it is more like a
range of times, within a confidence interval: for example, a system may be 95% confident that the
time now is between 10.3 and 10.5 seconds past the minute, but it doesn’t know any more precisely
than that [[58](ch08.html#Sheehy2015jm)].
If we only know the time +/– 100 ms, the microsecond digits in the timestamp are
essentially meaningless.