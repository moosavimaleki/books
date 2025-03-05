*  Frustration with the restrictiveness of relational schemas, and a desire for a more dynamic and
expressive data model [[5](ch02.html#Phillips2012we)] 
Different applications have different requirements, and the best choice of technology for one use
case may well be different from the best choice for another use case. It therefore seems likely that
in the foreseeable future, relational databases will continue to be used alongside a broad variety
of nonrelational datastores—an idea that is sometimes called polyglot persistence
[[3](ch02.html#nosql-distilled)]. ## The Object-Relational Mismatch 
Most application development today is done in object-oriented programming languages, which leads to
a common criticism of the SQL data model: if data is stored in relational tables, an awkward
translation layer is required between the objects in the application code and the database model of
tables, rows, and columns. The disconnect between the models is sometimes called an
impedance mismatch.[i](ch02.html#idm140605782666416) 
Object-relational mapping (ORM) frameworks like ActiveRecord and Hibernate reduce the amount of
boilerplate code required for this translation layer, but they can’t completely hide the differences
between the two models.