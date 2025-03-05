### Weak forms of lying Although we assume that nodes are generally honest, it can be worth adding mechanisms to software
that guard against weak forms of “lying”—for example, invalid messages due to hardware issues,
software bugs, and misconfiguration. Such protection mechanisms are not full-blown Byzantine fault
tolerance, as they would not withstand a determined adversary, but they are nevertheless simple and
pragmatic steps toward better reliability. For example: *  
Network packets do sometimes get corrupted due to hardware issues or bugs in operating systems,
drivers, routers, etc. Usually, corrupted packets are caught by the checksums built into TCP and
UDP, but sometimes they evade detection [[85](ch08.html#Gilman2015vp),
[86](ch08.html#Stone2000fc),
[87](ch08.html#Jones2015uy)].
Simple measures are usually sufficient protection against such corruption, such as checksums in
the application-level protocol. *  A publicly accessible application must carefully sanitize any inputs from users, for example
checking that a value is within a reasonable range and limiting the size of strings to prevent
denial of service through large memory allocations. An internal service behind a firewall may be
able to get away with less strict checks on inputs, but some basic sanity-checking of values (e.g.,
in protocol parsing [[85](ch08.html#Gilman2015vp)]) is a good idea.