# Formats for Encoding Data 
Programs usually work with data in (at least) two different representations: 1.  In memory, data is kept in objects, structs, lists, arrays, hash tables, trees, and so on. These
data structures are optimized for efficient access and manipulation by the CPU (typically using
pointers). 2.  When you want to write data to a file or send it over the network, you have to encode it as some
kind of self-contained sequence of bytes (for example, a JSON document). Since a pointer wouldn’t
make sense to any other process, this sequence-of-bytes representation looks quite different from
the data structures that are normally used in
memory.[i](ch04.html#idm140605777487312) 
Thus, we need some kind of translation between the two representations. The translation from the
in-memory representation to a byte sequence is called encoding (also known as serialization or
marshalling), and the reverse is called decoding (parsing, deserialization,
unmarshalling).[ii](ch04.html#idm140605777478016) # Terminology clash