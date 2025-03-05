When an application wants to decode some data (read it from a file or database, receive it from the
network, etc.), it is expecting the data to be in some schema, which is known as the reader’s
schema. That is the schema the application code is relying on—code may have been generated from
that schema during the application’s build process. The key idea with Avro is that the writer’s schema and the reader’s schema don’t have to be the
same—they only need to be compatible. When data is decoded (read), the Avro library resolves the
differences by looking at the writer’s schema and the reader’s schema side by side and translating
the data from the writer’s schema into the reader’s schema. The Avro specification
[[20](ch04.html#ApacheAvro)] defines exactly how this resolution works,
and it is illustrated in [Figure 4-6](#fig_encoding_avro_resolution). For example, it’s no problem if the writer’s schema and the reader’s schema have their fields in a
different order, because the schema resolution matches up the fields by field name. If the code
reading the data encounters a field that appears in the writer’s schema but not in the reader’s
schema, it is ignored. If the code reading the data expects some field, but the writer’s schema does
not contain a field of that name, it is filled in with a default value declared in the reader’s
schema.