
However, mathematical sets are not totally ordered: is {a, b} greater than
{b, c}? Well, you can’t really compare them, because neither is a subset of the other.
We say they are incomparable, and therefore mathematical sets are partially ordered: in some
cases one set is greater than another (if one set contains all the elements of another), but in
other cases they are incomparable. The difference between a total order and a partial order is reflected in different database
consistency models: Linearizability In a linearizable system, we have a total order of operations: if the system behaves as if there
is only a single copy of the data, and every operation is atomic, this means that for any two
operations we can always say which one happened first. This total ordering is illustrated as a
timeline in [Figure 9-4](#fig_consistency_linearizability_3). Causality We said that two operations are concurrent if neither happened before the other (see
[“The “happens-before” relationship and concurrency”](ch05.html#sec_replication_happens_before)). Put another way, two events are ordered if they are causally
related (one happened before the other), but they are incomparable if they are concurrent. This
means that causality defines a partial order, not a total order: some operations are ordered
with respect to each other, but some are incomparable.