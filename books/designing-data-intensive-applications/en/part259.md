So, we can see that although textual data formats such as JSON, XML, and CSV are widespread, binary
encodings based on schemas are also a viable option. They have a number of nice properties: *  They can be much more compact than the various “binary JSON” variants, since they can omit field
names from the encoded data. *  The schema is a valuable form of documentation, and because the schema is required for decoding,
you can be sure that it is up to date (whereas manually maintained documentation may easily
diverge from reality). *  Keeping a database of schemas allows you to check forward and backward compatibility of schema
changes, before anything is deployed. *  For users of statically typed programming languages, the ability to generate code from the schema
is useful, since it enables type checking at compile time. 
In summary, schema evolution allows the same kind of flexibility as schemaless/schema-on-read JSON
databases provide (see [“Schema flexibility in the document model”](ch02.html#sec_datamodels_schema_flexibility)), while also providing better
guarantees about your data and better tooling.