![ddia 0406](assets/ddia_0406.png) ###### Figure 4-6. An Avro reader resolves differences between the writer’s schema and the reader’s schema. ### Schema evolution rules With Avro, forward compatibility means that you can have a new version of the schema as writer and
an old version of the schema as reader. Conversely, backward compatibility means that you can have a
new version of the schema as reader and an old version as writer. To maintain compatibility, you may only add or remove a field that has a default value. (The field
favoriteNumber in our Avro schema has a default value of null.) For example, say you add a
field with a default value, so this new field exists in the new schema but not the old one. When a
reader using the new schema reads a record written with the old schema, the default value is filled
in for the missing field. If you were to add a field that has no default value, new readers wouldn’t be able to read data
written by old writers, so you would break backward compatibility. If you were to remove a field
that has no default value, old readers wouldn’t be able to read data written by new writers, so you
would break forward compatibility.