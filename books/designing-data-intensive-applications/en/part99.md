We will also see more on locality in [Chapter 3](ch03.html#ch_storage). ### Convergence of document and relational databases 
Most relational database systems (other than MySQL) have supported XML since the mid-2000s. This
includes functions to make local modifications to XML documents and the ability to index and query
inside XML documents, which allows applications to use data models very similar to what they would
do when using a document database. 
PostgreSQL since version 9.3 [[8](ch02.html#PostgreSQL2013)],
MySQL since version 5.7, and IBM DB2 since version 10.5
[[30](ch02.html#Cochrane2013ui)]
also have a similar level of support for JSON documents. Given the popularity of JSON for web APIs,
it is likely that other relational databases will follow in their footsteps and add JSON support. 
On the document database side, RethinkDB supports relational-like joins in its query language, and
some MongoDB drivers automatically resolve database references (effectively performing a client-side
join, although this is likely to be slower than a join performed in the database since it requires
additional network round-trips and is less optimized).