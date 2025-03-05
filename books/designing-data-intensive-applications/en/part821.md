The reducer can then perform the actual join logic easily: the reducer function is called once for
every user ID, and thanks to the secondary sort, the first value is expected to be the date-of-birth
record from the user database. The reducer stores the date of birth in a local variable and then
iterates over the activity events with the same user ID, outputting pairs of viewed-url and
viewer-age-in-years. Subsequent MapReduce jobs could then calculate the distribution of viewer ages
for each URL, and cluster by age group. Since the reducer processes all of the records for a particular user ID in one go, it only needs to
keep one user record in memory at any one time, and it never needs to make any requests over the
network. This algorithm is known as a sort-merge join, since mapper output is sorted by key, and
the reducers then merge together the sorted lists of records from both sides of the join.