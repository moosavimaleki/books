## Snapshot Isolation and Repeatable Read 
If you look superficially at read committed isolation, you could be forgiven for thinking that it
does everything that a transaction needs to do: it allows aborts (required for atomicity), it
prevents reading the incomplete results of transactions, and it prevents concurrent writes from
getting intermingled. Indeed, those are useful features, and much stronger guarantees than you can
get from a system that has no transactions. However, there are still plenty of ways in which you can have concurrency bugs when using this isolation level. For example, [Figure 7-6](#fig_transactions_item_many_preceders) illustrates a problem that can
occur with read committed. ![ddia 0706](assets/ddia_0706.png) ###### Figure 7-6. Read skew: Alice observes the database in an inconsistent state. Say Alice has $1,000 of savings at a bank, split across two accounts with $500 each. Now a
transaction transfers $100 from one of her accounts to the other. If she is unlucky enough to look at her
list of account balances in the same moment as that transaction is being processed, she may see one
account balance at a time before the incoming payment has arrived (with a balance of $500), and the
other account after the outgoing transfer has been made (the new balance being $400). To Alice it
now appears as though she only has a total of $900 in her accounts—it seems that $100 has
vanished into thin air.