Safety is often informally defined as nothing bad happens, and liveness as something good
eventually happens. However, it’s best to not read too much into those informal definitions,
because the meaning of good and bad is subjective. The actual definitions of safety and liveness are
precise and mathematical
[[90](ch08.html#Alpern1985dg)]: *  If a safety property is violated, we can point at a particular point in time at which it was
broken (for example, if the uniqueness property was violated, we can identify the particular
operation in which a duplicate fencing token was returned). After a safety property has been
violated, the violation cannot be undone—the damage is already done. *  A liveness property works the other way round: it may not hold at some point in time (for example,
a node may have sent a request but not yet received a response), but there is always hope that it
may be satisfied in the future (namely by receiving a response).