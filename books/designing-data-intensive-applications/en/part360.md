You may also set w and r to smaller numbers, so that w + r ≤ n (i.e.,
the quorum condition is not satisfied). In this case, reads and writes will still be sent to n
nodes, but a smaller number of successful responses is required for the operation to succeed. With a smaller w and r you are more likely to read stale values, because it’s more likely that
your read didn’t include the node with the latest value. On the upside, this configuration allows
lower latency and higher availability: if there is a network interruption and many replicas become
unreachable, there’s a higher chance that you can continue processing reads and writes. Only after
the number of reachable replicas falls below w or r does the database become unavailable for
writing or reading, respectively. However, even with w + r > n, there are likely to be edge cases where stale
values are returned. These depend on the implementation, but possible scenarios include: