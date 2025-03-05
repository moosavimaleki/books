![ddia 0407](assets/ddia_0407.png) ###### Figure 4-7. When an older version of the application updates data previously written by a newer version of the application, data may be lost if you’re not careful. ### Different values written at different times A database generally allows any value to be updated at any time. This means that within a single
database you may have some values that were written five milliseconds ago, and some values that were
written five years ago. When you deploy a new version of your application (of a server-side application, at least), you may
entirely replace the old version with the new version within a few minutes. The same is not true of
database contents: the five-year-old data will still be there, in the original encoding, unless you
have explicitly rewritten it since then. This observation is sometimes summed up as data outlives
code. 
Rewriting (migrating) data into a new schema is certainly possible, but it’s an expensive thing to
do on a large dataset, so most databases avoid it if possible. Most relational databases allow
simple schema changes, such as adding a new column with a null default value, without rewriting
existing data.[v](ch04.html#idm140605776834848) When an old row is
read, the database fills in nulls for any columns that are missing from the encoded data on disk.

LinkedIn’s document database Espresso uses Avro for storage, allowing it to use Avro’s schema
evolution rules [[23](ch04.html#Auradkar2015wz)].