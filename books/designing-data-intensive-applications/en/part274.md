*  The client and the service may be implemented in different programming languages, so the RPC
framework must translate datatypes from one language into another. This can end up ugly, since not
all languages have the same types—recall JavaScript’s problems with numbers greater than 253,
for example (see [“JSON, XML, and Binary Variants”](#sec_encoding_json)). This problem doesn’t exist in a single process written in
a single language. All of these factors mean that there’s no point trying to make a remote service look too much like a
local object in your programming language, because it’s a fundamentally different thing. Part of the
appeal of REST is that it doesn’t try to hide the fact that it’s a network protocol (although this
doesn’t seem to stop people from building RPC libraries on top of REST). ### Current directions for RPC 
Despite all these problems, RPC isn’t going away. Various RPC frameworks have been built on top of
all the encodings mentioned in this chapter: for example, Thrift and Avro come with RPC support
included, gRPC is an RPC implementation using Protocol Buffers, Finagle also uses Thrift, and Rest.li
uses JSON over HTTP.