
The ideas on which these encodings are based are by no means new. For example, they have a lot in
common with ASN.1, a schema definition language that was first standardized in 1984
[[27](ch04.html#Larmouth1999)].
It was used to define various network protocols, and its binary encoding (DER) is still used to encode
SSL certificates (X.509), for example
[[28](ch04.html#Housley1999tv)].
ASN.1 supports schema evolution using tag numbers, similar to Protocol Buffers and Thrift
[[29](ch04.html#Walkin2010ur)].
However, it’s also very complex and badly documented, so ASN.1
is probably not a good choice for new applications. 
Many data systems also implement some kind of proprietary binary encoding for their data. For
example, most relational databases have a network protocol over which you can send queries to the
database and get back responses. Those protocols are generally specific to a particular database,
and the database vendor provides a driver (e.g., using the ODBC or JDBC APIs) that decodes responses
from the database’s network protocol into in-memory data structures.