*  NTP synchronization can only be as good as the network delay, so there is a limit to its
accuracy when you’re on a congested network with variable packet delays. One experiment showed
that a minimum error of 35 ms is achievable when synchronizing over the internet
[[42](ch08.html#Caporaloni2012jn)],
though occasional spikes in network delay lead to errors of around a second. Depending on the
configuration, large network delays can cause the NTP client to give up entirely. *  Some NTP servers are wrong or misconfigured, reporting time that is off by hours
[[43](ch08.html#Minar1999vf), [44](ch08.html#Holub2014uc)].
NTP clients are quite robust, because they query several servers and ignore outliers.
Nevertheless, it’s somewhat worrying to bet the correctness of your systems on the time that you
were told by a stranger on the internet. *  
Leap seconds result in a minute that is 59 seconds or 61 seconds long, which messes up timing
assumptions in systems that are not designed with leap seconds in mind
[[45](ch08.html#Kamp2011cr)].

The fact that leap seconds have crashed many large systems
[[38](ch08.html#GrahamCumming2017db),
[46](ch08.html#Minar2012vh_ch8)]
shows how easy it is for incorrect assumptions about clocks to sneak into a system. The best
way of handling leap seconds may be to make NTP servers “lie,” by performing the leap second
adjustment gradually over the course of a day (this is known as smearing)
[[47](ch08.html#Pascoe2011uj),
[48](ch08.html#Zhao2015ws)],
although actual NTP server behavior varies in practice
[[49](ch08.html#Veitch2016jw)].