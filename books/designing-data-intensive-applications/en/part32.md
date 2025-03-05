
Counterintuitively, in such fault-tolerant systems, it can make sense to increase the rate of
faults by triggering them deliberately—for example, by randomly killing individual processes
without warning. Many critical bugs are actually due to poor error handling
[[3](ch01.html#Yuan2014va)]; by deliberately inducing faults, you ensure
that the fault-tolerance machinery is continually exercised and tested, which can increase your
confidence that faults will be handled correctly when they occur naturally. The Netflix Chaos
Monkey [[4](ch01.html#netflix-simian-army)] is an example of this approach. Although we generally prefer tolerating faults over preventing faults, there are cases where
prevention is better than cure (e.g., because no cure exists). This is the case with security
matters, for example: if an attacker has compromised a system and gained access to sensitive data,
that event cannot be undone. However, this book mostly deals with the kinds of faults that can be
cured, as described in the following sections. ## Hardware Faults