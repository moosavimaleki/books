
Avro provides optional code generation for statically typed programming languages, but it can be
used just as well without any code generation. If you have an object container file (which embeds
the writer’s schema), you can simply open it using the Avro library and look at the data in the
same way as you could look at a JSON file. The file is self-describing since it includes all the
necessary metadata. This property is especially useful in conjunction with dynamically typed data processing languages like
Apache Pig [[26](ch04.html#ApachePig)]. In Pig, you can just open
some Avro files, start analyzing them, and write derived datasets to output files in Avro format
without even thinking about schemas. ## The Merits of Schemas 
As we saw, Protocol Buffers, Thrift, and Avro all use a schema to describe a binary encoding format.
Their schema languages are much simpler than XML Schema or JSON Schema, which support much more
detailed validation rules (e.g., “the string value of this field must match this regular expression”
or “the integer value of this field must be between 0 and 100”). As Protocol Buffers, Thrift, and
Avro are simpler to implement and simpler to use, they have grown to support a fairly wide range of
programming languages.