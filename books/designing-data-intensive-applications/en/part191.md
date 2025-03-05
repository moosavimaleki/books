Further changes to storage engine design will probably be needed if non-volatile memory (NVM)
technologies become more widely adopted
[[46](ch03.html#Arulraj2015gs)].
At present, this is a new area of research, but it is worth keeping an eye on in the future. # Transaction Processing or Analytics? 
In the early days of business data processing, a write to the database typically corresponded to a
commercial transaction taking place: making a sale, placing an order with a supplier, paying an
employee’s salary, etc. As databases expanded into areas that didn’t involve money changing hands,
the term transaction nevertheless stuck, referring to a group of reads and writes that form a
logical unit. ###### Note 
A transaction needn’t necessarily have ACID (atomicity, consistency, isolation, and durability)
properties. Transaction processing just means allowing clients to make low-latency reads and
writes—as opposed to batch processing jobs, which only run periodically (for example, once per
day). We discuss the ACID properties in [Chapter 7](ch07.html#ch_transactions) and batch processing in [Chapter 10](ch10.html#ch_batch).