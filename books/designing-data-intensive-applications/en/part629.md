[iv](ch08.html#idm140605760878336-marker) Peering
agreements between internet service providers and the establishment of routes through the Border
Gateway Protocol (BGP), bear closer resemblance to circuit switching than IP itself. At this level,
it is possible to buy dedicated bandwidth. However, internet routing operates at the level of
networks, not individual connections between hosts, and at a much longer timescale. [v](ch08.html#idm140605760841440-marker) Although
the clock is called real-time, it has nothing to do with real-time operating systems, as
discussed in [“Response time guarantees”](#sec_distributed_clocks_realtime). [vi](ch08.html#idm140605760654304-marker) There are distributed sequence
number generators, such as Twitter’s Snowflake, that generate approximately monotonically
increasing unique IDs in a scalable way (e.g., by allocating blocks of the ID space to different
nodes).  However, they typically cannot guarantee an ordering that is consistent with causality,
because the timescale at which blocks of IDs are assigned is longer than the timescale of database
reads and writes. See also [“Ordering Guarantees”](ch09.html#sec_consistency_ordering). ##### References