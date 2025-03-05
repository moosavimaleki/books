
Hive’s skewed join optimization takes an alternative approach. It requires hot keys to be specified
explicitly in the table metadata, and it stores records related to those keys in separate files from
the rest. When performing a join on that table, it uses a map-side join (see the next section) for
the hot keys. When grouping records by a hot key and aggregating them, you can perform the grouping in two
stages. The first MapReduce stage sends records to a random reducer, so that each reducer performs
the grouping on a subset of records for the hot key and outputs a more compact aggregated value
per key. The second MapReduce job then combines the values from all of the first-stage reducers into
a single value per key. ## Map-Side Joins 
The join algorithms described in the last section perform the actual join logic in the reducers, and
are hence known as reduce-side joins. The mappers take the role of preparing the input data:
extracting the key and value from each input record, assigning the key-value pairs to a reducer
partition, and sorting by key.