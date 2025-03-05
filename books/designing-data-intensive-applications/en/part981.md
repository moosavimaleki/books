Such time dependence can occur in many places. For example, if you sell things, you need to apply
the right tax rate to invoices, which depends on the country or state, the type of product, and the
date of sale (since tax rates change from time to time). When joining sales to a table of tax rates,
you probably want to join with the tax rate at the time of the sale, which may be different from the
current tax rate if you are reprocessing historical data. If the ordering of events across streams is undetermined, the join becomes nondeterministic
[[87](ch11.html#Kirwin2014vm)], which means you cannot
rerun the same job on the same input and necessarily get the same result: the events on the input
streams may be interleaved in a different way when you run the job again. 
In data warehouses, this issue is known as a slowly changing dimension (SCD), and it is often
addressed by using a unique identifier for a particular version of the joined record: for example,
every time the tax rate changes, it is given a new identifier, and the invoice includes the
identifier for the tax rate at the time of sale
[[88](ch11.html#Helland2005tc_ch11), [89](ch11.html#Kimball2013tb_ch11)]. This change makes the join
deterministic, but has the consequence that log compaction is not possible, since all versions of
the records in the table need to be retained.