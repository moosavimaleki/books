
Most document databases, and the JSON support in relational databases, do not enforce any schema on
the data in documents. XML support in relational databases usually comes with optional schema
validation. No schema means that arbitrary keys and values can be added to a document, and when
reading, clients have no guarantees as to what fields the documents may contain. 
Document databases are sometimes called schemaless, but that’s misleading, as the code that reads
the data usually assumes some kind of structure—i.e., there is an implicit schema, but it is not
enforced by the database [[20](ch02.html#Fowler2013uq)]. A more accurate term is schema-on-read (the structure
of the data is implicit, and only interpreted when the data is read), in contrast with
schema-on-write (the traditional approach of relational databases, where the schema is explicit
and the database ensures all written data conforms to it)
[[21](ch02.html#Awadallah2009vi)]. 
Schema-on-read is similar to dynamic (runtime) type checking in programming languages, whereas
schema-on-write is similar to static (compile-time) type checking. Just as the advocates of static
and dynamic type checking have big debates about their relative merits
[[22](ch02.html#Odersky2013wz)],
enforcement of schemas in database is a contentious topic, and in general there’s no right or wrong
answer.