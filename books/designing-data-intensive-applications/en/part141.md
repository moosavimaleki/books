[iii](ch02.html#idm140605782440736-marker) At the time of
writing, joins are supported in RethinkDB, not supported in MongoDB, and only supported in
predeclared views in CouchDB. [iv](ch02.html#idm140605782388832-marker) Foreign key constraints allow you to
restrict modifications, but such constraints are not required by the relational model. Even with
constraints, joins on foreign keys are performed at query time, whereas in CODASYL, the join was
effectively done at insert time. [v](ch02.html#idm140605782034240-marker) Codd’s original description of the
relational model [[1](ch02.html#Codd1970dg)] actually allowed
something quite similar to JSON documents within a relational schema. He called it nonsimple
domains. The idea was that a value in a row doesn’t have to just be a primitive datatype like a
number or a string, but could also be a nested relation (table)—so you can have an
arbitrarily nested tree structure as a value, much like the JSON or XML support that was added to
SQL over 30 years later. [vi](ch02.html#idm140605782079584-marker) IMS and
CODASYL both used imperative query APIs. Applications typically used COBOL code to iterate over
records in the database, one record at a time
[[2](ch02.html#Stonebraker2005wv),
[16](ch02.html#Knowles1984tm)].