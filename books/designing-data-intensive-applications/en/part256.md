### Code generation and dynamically typed languages 
Thrift and Protocol Buffers rely on code generation: after a schema has been defined, you can
generate code that implements this schema in a programming language of your choice. This is useful
in statically typed languages such as Java, C++, or C#, because it allows efficient in-memory
structures to be used for decoded data, and it allows type checking and autocompletion in IDEs when
writing programs that access the data structures. 
In dynamically typed programming languages such as JavaScript, Ruby, or Python, there is not much
point in generating code, since there is no compile-time type checker to satisfy. Code generation is
often frowned upon in these languages, since they otherwise avoid an explicit compilation step.
Moreover, in the case of a dynamically generated schema (such as an Avro schema generated from a
database table), code generation is an unnecessarily obstacle to getting to the data.