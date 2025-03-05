
Both Thrift and Protocol Buffers require a schema for any data that is encoded. To encode the data
in [Example 4-1](#fig_encoding_json) in Thrift, you would describe the schema in the Thrift interface
definition language (IDL) like this: ```
`struct` `Person` `{`
  `1``:` `required` `string`       `userName``,`
  `2``:` `optional` `i64`          `favoriteNumber``,`
  `3``:` `optional` `list``<``string``>` `interests`
`}`
``` The equivalent schema definition for Protocol Buffers looks very similar: ```
`message` `Person` `{`
    `required` `string` `user_name`       `=` `1``;`
    `optional` `int64`  `favorite_number` `=` `2``;`
    `repeated` `string` `interests`       `=` `3``;`
`}`
``` 
Thrift and Protocol Buffers each come with a code generation tool that takes a schema definition
like the ones shown here, and produces classes that implement the schema in various programming languages
[[18](ch04.html#ThriftLangs)]. Your application code can call this generated code to encode
or decode records of the schema. 
What does data encoded with this schema look like? Confusingly, Thrift has two different binary
encoding formats,[iii](ch04.html#idm140605777137376)
called BinaryProtocol and CompactProtocol, respectively. Let’s look at BinaryProtocol first.
Encoding [Example 4-1](#fig_encoding_json) in that format takes 59 bytes, as shown in
[Figure 4-2](#fig_encoding_thrift_binary) [[19](ch04.html#Kleppmann2012tu)].