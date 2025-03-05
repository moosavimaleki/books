Now, if the database schema changes (for example, a table has one column added and one column
removed), you can just generate a new Avro schema from the updated database schema and export data in
the new Avro schema. The data export process does not need to pay any attention to the schema
change—it can simply do the schema conversion every time it runs. Anyone who reads the new data
files will see that the fields of the record have changed, but since the fields are identified by
name, the updated writer’s schema can still be matched up with the old reader’s schema. By contrast, if you were using Thrift or Protocol Buffers for this purpose, the field tags would
likely have to be assigned by hand: every time the database schema changes, an administrator would
have to manually update the mapping from database column names to field tags. (It might be possible
to automate this, but the schema generator would have to be very careful to not assign previously
used field tags.) This kind of dynamically generated schema simply wasn’t a design goal of Thrift or
Protocol Buffers, whereas it was for Avro.