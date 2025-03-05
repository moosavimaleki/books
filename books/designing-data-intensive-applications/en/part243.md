As you can see from the examples, an encoded record is just the concatenation of its encoded fields.
Each field is identified by its tag number (the numbers 1, 2, 3 in the sample schemas) and
annotated with a datatype (e.g., string or integer). If a field value is not set, it is simply
omitted from the encoded record. From this you can see that field tags are critical to the meaning
of the encoded data. You can change the name of a field in the schema, since the encoded data never
refers to field names, but you cannot change a field’s tag, since that would make all existing
encoded data invalid. You can add new fields to the schema, provided that you give each field a new tag number. If old
code (which doesn’t know about the new tag numbers you added) tries to read data written by new
code, including a new field with a tag number it doesn’t recognize, it can simply ignore that field.
The datatype annotation allows the parser to determine how many bytes it needs to skip. This
maintains forward compatibility: old code can read records that were written by new code.