![ddia 0402](assets/ddia_0402.png) ###### Figure 4-2. Example record encoded using Thrift’s BinaryProtocol. 
Similarly to [Figure 4-1](#fig_encoding_messagepack), each field has a type annotation (to indicate whether it
is a string, integer, list, etc.) and, where required, a length indication (length of a string,
number of items in a list). The strings that appear in the data (“Martin”, “daydreaming”, “hacking”)
are also encoded as ASCII (or rather, UTF-8), similar to before. 
The big difference compared to [Figure 4-1](#fig_encoding_messagepack) is that there are no field names
(userName, favoriteNumber, interests). Instead, the encoded data contains field tags, which
are numbers (1, 2, and 3). Those are the numbers that appear in the schema definition. Field tags
are like aliases for fields—they are a compact way of saying what field we’re talking about,
without having to spell out the field name. 
The Thrift CompactProtocol encoding is semantically equivalent to BinaryProtocol, but as you can see
in [Figure 4-3](#fig_encoding_thrift_compact), it packs the same information into only 34 bytes. It does this
by packing the field type and tag number into a single byte, and by using variable-length integers.
Rather than using a full eight bytes for the number 1337, it is encoded in two bytes, with the top bit
of each byte used to indicate whether there are still more bytes to come. This means numbers between –64
and 63 are encoded in one byte, numbers between –8192 and 8191 are encoded in two bytes, etc. Bigger
numbers use more bytes.