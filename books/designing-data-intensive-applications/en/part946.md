### Advantages of immutable events 
Immutability in databases is an old idea. For example, accountants have been using immutability for
centuries in financial bookkeeping. When a transaction occurs, it is recorded in an append-only
ledger, which is essentially a log of events describing money, goods, or services that have changed
hands. The accounts, such as profit and loss or the balance sheet, are derived from the transactions
in the ledger by adding them up [[53](ch11.html#Kleppmann2011vr)]. 
If a mistake is made, accountants don’t erase or change the incorrect transaction in the
ledger—instead, they add another transaction that compensates for the mistake, for example refunding
an incorrect charge. The incorrect transaction still remains in the ledger forever, because it might
be important for auditing reasons. If incorrect figures, derived from the incorrect ledger, have
already been published, then the figures for the next accounting period include a correction. This
process is entirely normal in accounting [[54](ch11.html#Helland2007vk)].