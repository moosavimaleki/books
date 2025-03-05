Thrift has a dedicated list datatype, which is parameterized with the datatype of the list
elements. This does not allow the same evolution from single-valued to multi-valued as Protocol
Buffers does, but it has the advantage of supporting nested lists. ## Avro 
Apache Avro
[[20](ch04.html#ApacheAvro)] is another binary
encoding format that is interestingly different from Protocol Buffers and Thrift. It was started in
2009 as a subproject of Hadoop, as a result of Thrift not being a good fit for Hadoop’s use cases
[[21](ch04.html#Cutting2009tu)]. 
Avro also uses a schema to specify the structure of the data being encoded. It has two schema
languages: one (Avro IDL) intended for human editing, and one (based on JSON) that is more easily
machine-readable. Our example schema, written in Avro IDL, might look like this: ```
`record` `Person` `{`
    `string`               `userName``;`
    `union` `{` `null``,` `long` `}` `favoriteNumber` `=` `null``;`
    `array``<``string``>`        `interests``;`
`}`
``` 
The equivalent JSON representation of that schema is as follows: