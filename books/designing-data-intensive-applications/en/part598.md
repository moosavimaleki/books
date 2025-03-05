
An emerging idea is to treat GC pauses like brief planned outages of a node, and to let other nodes
handle requests from clients while one node is collecting its garbage. If the runtime can warn the
application that a node soon requires a GC pause, the application can stop sending new requests to
that node, wait for it to finish processing outstanding requests, and then perform the GC while no
requests are in progress. This trick hides GC pauses from clients and reduces the high percentiles of
response time [[70](ch08.html#Terei2015va),
[71](ch08.html#Maas2015vf)].
Some latency-sensitive financial trading systems
[[72](ch08.html#Cinnober2013up)]
use this approach. A variant of this idea is to use the garbage collector only for short-lived objects (which are fast
to collect) and to restart processes periodically, before they accumulate enough long-lived objects
to require a full GC of long-lived objects [[65](ch08.html#Thompson2013vj),
[73](ch08.html#Fowler2011wp_ch8)]. One node can be restarted at a time, and traffic can
be shifted away from the node before the planned restart, like in a rolling upgrade (see
[Chapter 4](ch04.html#ch_encoding)).