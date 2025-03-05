Database with individually written records In a database, different records may be written at different points in time using different
writer’s schemas—you cannot assume that all the records will have the same schema. The simplest
solution is to include a version number at the beginning of every encoded record, and to keep a
list of schema versions in your database. A reader can fetch a record, extract the version number,
and then fetch the writer’s schema for that version number from the database. Using that writer’s
schema, it can decode the rest of the record.
 (Espresso
[[23](ch04.html#Auradkar2015wz)]
works this way, for example.) Sending records over a network connection 
When two processes are communicating over a bidirectional network connection, they can negotiate
the schema version on connection setup and then use that schema for the lifetime of the
connection. The Avro RPC protocol (see [“Dataflow Through Services: REST and RPC”](#sec_encoding_dataflow_rpc)) works like this.