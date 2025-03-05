Although such auditability is particularly important in financial systems, it is also beneficial for
many other systems that are not subject to such strict regulation. As discussed in
[“Philosophy of batch process outputs”](ch10.html#sec_batch_philosophy), if you accidentally deploy buggy code that writes bad data to a database,
recovery is much harder if the code is able to destructively overwrite data. With an append-only log
of immutable events, it is much easier to diagnose what happened and recover from the problem. Immutable events also capture more information than just the current state. For example, on a
shopping website, a customer may add an item to their cart and then remove it again. Although the
second event cancels out the first event from the point of view of order fulfillment, it may be
useful to know for analytics purposes that the customer was considering a particular item but then
decided against it. Perhaps they will choose to buy it in the future, or perhaps they found a
substitute. This information is recorded in an event log, but would be lost in a database that
deletes items when they are removed from the cart
[[42](ch11.html#Young2014wp)].