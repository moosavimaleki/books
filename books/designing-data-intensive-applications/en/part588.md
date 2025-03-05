
Can we use the timestamps from synchronized time-of-day clocks as transaction IDs? If we could get
the synchronization good enough, they would have the right properties: later transactions have a
higher timestamp. The problem, of course, is the uncertainty about clock accuracy. 
Spanner implements snapshot isolation across datacenters in this way
[[59](ch08.html#Demirbas2013uz),
[60](ch08.html#Malkhi2013bl)].
It uses the clock’s confidence interval as reported by the TrueTime API, and is based on the
following observation: if you have two confidence intervals, each consisting of an earliest and
latest possible timestamp (A = [Aearliest, Alatest] and
B = [Bearliest, Blatest]), and those two intervals do not overlap (i.e.,
Aearliest < Alatest < Bearliest < Blatest), then B definitely happened after A—there
can be no doubt. Only if the intervals overlap are we unsure in which order A and B happened. 
In order to ensure that transaction timestamps reflect causality, Spanner deliberately waits for the
length of the confidence interval before committing a read-write transaction. By doing so, it
ensures that any transaction that may read the data is at a sufficiently later time, so their
confidence intervals do not overlap. In order to keep the wait time as short as possible, Spanner
needs to keep the clock uncertainty as small as possible; for this purpose, Google deploys a GPS
receiver or atomic clock in each datacenter, allowing clocks to be synchronized to within about
7 ms [[41](ch08.html#Corbett2012uz_ch8)].