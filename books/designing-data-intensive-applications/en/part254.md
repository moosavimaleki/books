
A database of schema versions is a useful thing to have in any case, since it acts as documentation
and gives you a chance to check schema compatibility
[[24](ch04.html#Kreps2015ux)].
As the version number, you could use a simple incrementing integer, or you could use a hash of the
schema. ### Dynamically generated schemas 
One advantage of Avro’s approach, compared to Protocol Buffers and Thrift, is that the schema
doesn’t contain any tag numbers. But why is this important? What’s the problem with keeping a couple
of numbers in the schema? The difference is that Avro is friendlier to dynamically generated schemas. For example, say
you have a relational database whose contents you want to dump to a file, and you want to use a
binary format to avoid the aforementioned problems with textual formats (JSON, CSV, SQL). If you use
Avro, you can fairly easily generate an Avro schema (in the JSON representation we saw earlier) from the
relational schema and encode the database contents using that schema, dumping it all to an Avro
object container file [[25](ch04.html#Shapira2014wf)]. You generate a record schema
for each database table, and each column becomes a field in that record. The column name in the
database maps to the field name in Avro.