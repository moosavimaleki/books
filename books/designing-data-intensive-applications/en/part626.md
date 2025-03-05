Once a fault is detected, making a system tolerate it is not easy either: there is no global
variable, no shared memory, no common knowledge or any other kind of shared state between the
machines. Nodes can’t even agree on what time it is, let alone on anything more profound. The only way
information can flow from one node to another is by sending it over the unreliable network. Major
decisions cannot be safely made by a single node, so we require protocols that enlist help from
other nodes and try to get a quorum to agree. If you’re used to writing software in the idealized mathematical perfection of a single computer,
where the same operation always deterministically returns the same result, then moving to the messy
physical reality of distributed systems can be a bit of a shock. Conversely, distributed systems
engineers will often regard a problem as trivial if it can be solved on a single computer
[[5](ch08.html#Hodges2013tj)],
and indeed a single computer can do a lot nowadays
[[95](ch08.html#McSherry2015vx_ch8)]. If you can avoid opening Pandora’s box and simply keep things on a
single machine, it is generally worth doing so.