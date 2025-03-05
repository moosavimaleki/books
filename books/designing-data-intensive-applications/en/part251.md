
In some programming languages, null is an acceptable default for any variable, but this is not the
case in Avro: if you want to allow a field to be null, you have to use a union type. For example,
union { null, long, string } field; indicates that field can be a number, or a string, or null.
You can only use null as a default value if it is one of the branches of the
union.[iv](ch04.html#idm140605776974416) This is a little more verbose than having
everything nullable by default, but it helps prevent bugs by being explicit about what can and
cannot be null [[22](ch04.html#Hoare2009vv)]. Consequently, Avro doesn’t have optional and required markers in the same way as Protocol
Buffers and Thrift do (it has union types and default values instead). Changing the datatype of a field is possible, provided that Avro can convert the type. Changing the
name of a field is possible but a little tricky: the reader’s schema can contain aliases for field
names, so it can match an old writer’s schema field names against the aliases. This means that
changing a field name is backward compatible but not forward compatible. Similarly, adding a branch
to a union type is backward compatible but not forward compatible.