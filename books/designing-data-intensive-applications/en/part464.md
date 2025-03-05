
However, what happens if the earlier write is part of a transaction that has not yet committed, so
the later write overwrites an uncommitted value? This is called a dirty write
[[28](ch07.html#Berenson1995kj)]. Transactions running at the read
committed isolation level must prevent dirty writes, usually by delaying the second write until the
first write’s transaction has committed or aborted. By preventing dirty writes, this isolation level avoids some kinds of concurrency problems: *  If transactions update multiple objects, dirty writes can lead to a bad outcome. For example,
consider [Figure 7-5](#fig_transactions_dirty_writes), which illustrates a used car sales website on which
two people, Alice and Bob, are simultaneously trying to buy the same car. Buying a car requires
two database writes: the listing on the website needs to be updated to reflect the buyer, and the
sales invoice needs to be sent to the buyer. In the case of [Figure 7-5](#fig_transactions_dirty_writes),
the sale is awarded to Bob (because he performs the winning update to the listings table), but the
invoice is sent to Alice (because she performs the winning update to the invoices table). Read
committed prevents such mishaps.