### Detecting writes that affect prior reads 
The second case to consider is when another transaction modifies data after it has been read. This
case is illustrated in [Figure 7-11](#fig_transactions_detect_index_range). ![ddia 0711](assets/ddia_0711.png) ###### Figure 7-11. In serializable snapshot isolation, detecting when one transaction modifies another transaction’s reads. In the context of two-phase locking we discussed index-range locks (see
[“Index-range locks”](#sec_transactions_2pl_range)), which allow the database to lock access to all rows matching some
search query, such as WHERE shift_id = 1234. We can use a similar technique here, except that SSI
locks don’t block other transactions. 
In [Figure 7-11](#fig_transactions_detect_index_range), transactions 42 and 43 both search for on-call doctors
during shift 1234. If there is an index on shift_id, the database can use the index entry 1234 to
record the fact that transactions 42 and 43 read this data. (If there is no index, this information
can be tracked at the table level.) This information only needs to be kept for a while: after a
transaction has finished (committed or aborted), and all concurrent transactions have finished, the
database can forget what data it read.