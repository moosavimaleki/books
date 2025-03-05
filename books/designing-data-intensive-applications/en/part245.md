### Datatypes and schema evolution 
What about changing the datatype of a field? That may be possible—check the documentation for
details—but there is a risk that values will lose precision or get truncated. For example, say you
change a 32-bit integer into a 64-bit integer. New code can easily read data written by old code,
because the parser can fill in any missing bits with zeros. However, if old code reads data written
by new code, the old code is still using a 32-bit variable to hold the value. If the decoded 64-bit
value won’t fit in 32 bits, it will be truncated. A curious detail of Protocol Buffers is that it does not have a list or array datatype, but instead
has a repeated marker for fields (which is a third option alongside required and optional). As
you can see in [Figure 4-4](#fig_encoding_protobuf), the encoding of a repeated field is just what it says on
the tin: the same field tag simply appears multiple times in the record. This has the nice effect
that it’s okay to change an optional (single-valued) field into a repeated (multi-valued) field.
New code reading old data sees a list with zero or one elements (depending on whether the field was
present); old code reading new data sees only the last element of the list.