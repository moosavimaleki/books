
However, if your application does use many-to-many relationships, the document model becomes less
appealing. It’s possible to reduce the need for joins by denormalizing, but then the application
code needs to do additional work to keep the denormalized data consistent. Joins can be emulated in
application code by making multiple requests to the database, but that also moves complexity into
the application and is usually slower than a join performed by specialized code inside the
database. In such cases, using a document model can lead to significantly more complex application
code and worse performance [[15](ch02.html#Mei2013vz)]. It’s not possible to say in general which data model leads to simpler application code; it depends
on the kinds of relationships that exist between data items. For highly interconnected data, the
document model is awkward, the relational model is acceptable, and graph models (see
[“Graph-Like Data Models”](#sec_datamodels_graph)) are the most natural. ### Schema flexibility in the document model