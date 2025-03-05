### Diversity of storage 
Databases require you to structure data according to a particular model (e.g., relational or
documents), whereas files in a distributed filesystem are just byte sequences, which can be written
using any data model and encoding. They might be collections of database records, but they can
equally well be text, images, videos, sensor readings, sparse matrices, feature vectors, genome
sequences, or any other kind of data. 
To put it bluntly, Hadoop opened up the possibility of indiscriminately dumping data into HDFS, and
only later figuring out how to process it further
[[53](ch10.html#Kreps2014qz)]. By
contrast, MPP databases typically require careful up-front modeling of the data and query patterns
before importing the data into the database’s proprietary storage format. From a purist’s point of view, it may seem that this careful modeling and import is desirable, because
it means users of the database have better-quality data to work with. However, in practice, it
appears that simply making data available quickly—even if it is in a quirky, difficult-to-use,
raw format—is often more valuable than trying to decide on the ideal data model up front
[[54](ch10.html#Cohen2009fv)].