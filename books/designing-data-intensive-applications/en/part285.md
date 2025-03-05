
We discussed several data encoding formats and their compatibility properties: *  Programming language–specific encodings are restricted to a single programming language and often
fail to provide forward and backward compatibility. *  Textual formats like JSON, XML, and CSV are widespread, and their compatibility depends on how you
use them. They have optional schema languages, which are sometimes helpful and sometimes a
hindrance. These formats are somewhat vague about datatypes, so you have to be careful with things
like numbers and binary strings. *  Binary schema–driven formats like Thrift, Protocol Buffers, and Avro allow compact, efficient
encoding with clearly defined forward and backward compatibility semantics. The schemas can be
useful for documentation and code generation in statically typed languages. However, they have the
downside that data needs to be decoded before it is human-readable. We also discussed several modes of dataflow, illustrating different scenarios in which data
encodings are important: * 