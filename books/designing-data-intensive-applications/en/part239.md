3.  The next eight bytes are the field name userName in ASCII. Since the length was indicated
previously, there’s no need for any marker to tell us where the string ends (or any escaping). 4.  The next seven bytes encode the six-letter string value Martin with a prefix 0xa6, and so on. The binary encoding is 66 bytes long, which is only a little less than the 81 bytes taken by the
textual JSON encoding (with whitespace removed). All the binary encodings of JSON are similar in
this regard. It’s not clear whether such a small space reduction (and perhaps a speedup in parsing)
is worth the loss of human-readability. In the following sections we will see how we can do much better, and encode the same record in just
32 bytes. ![ddia 0401](assets/ddia_0401.png) ###### Figure 4-1. Example record ([Example 4-1](#fig_encoding_json)) encoded using MessagePack. ## Thrift and Protocol Buffers 
Apache Thrift [[15](ch04.html#Slee2007vh)]
and Protocol Buffers (protobuf)
[[16](ch04.html#GoogleProtobuf)]
are binary encoding libraries that are based on the same principle. Protocol Buffers was originally
developed at Google, Thrift was originally developed at Facebook, and both were made open source in
2007–08 [[17](ch04.html#Anishchenko2012tx)].