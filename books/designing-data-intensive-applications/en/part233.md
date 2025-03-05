*  In order to restore data in the same object types, the decoding process needs to be able to
instantiate arbitrary classes. This is frequently a source of security problems
[[5](ch04.html#CWE502)]: if an attacker can get your application to decode an arbitrary
byte sequence, they can instantiate arbitrary classes, which in turn often allows them to do
terrible things such as remotely executing arbitrary code
[[6](ch04.html#Breen2015up),
[7](ch04.html#McKenzie2013uv)]. *  Versioning data is often an afterthought in these libraries: as they are intended for quick and
easy encoding of data, they often neglect the inconvenient problems of forward and backward
compatibility. *  Efficiency (CPU time taken to encode or decode, and the size of the encoded structure) is also
often an afterthought. For example, Java’s built-in serialization is notorious for its bad
performance and bloated encoding [[8](ch04.html#JvmSerializers)]. For these reasons it’s generally a bad idea to use your language’s built-in encoding for anything
other than very transient purposes.