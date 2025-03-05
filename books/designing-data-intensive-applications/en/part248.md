![ddia 0405](assets/ddia_0405.png) ###### Figure 4-5. Example record encoded using Avro. To parse the binary data, you go through the fields in the order that they appear in the schema and
use the schema to tell you the datatype of each field. This means that the binary data can only be
decoded correctly if the code reading the data is using the exact same schema as the code that
wrote the data. Any mismatch in the schema between the reader and the writer would mean incorrectly
decoded data. So, how does Avro support schema evolution? ### The writer’s schema and the reader’s schema 
With Avro, when an application wants to encode some data (to write it to a file or database, to send
it over the network, etc.), it encodes the data using whatever version of the schema it knows
about—for example, that schema may be compiled into the application. This is known as the
writer’s schema.