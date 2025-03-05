Databases, where the process writing to the database encodes the data and the process reading
from the database decodes it *  RPC and REST APIs, where the client encodes a request, the server decodes the request and encodes
a response, and the client finally decodes the response *  Asynchronous message passing (using message brokers or actors), where nodes communicate by sending
each other messages that are encoded by the sender and decoded by the recipient We can conclude that with a bit of care, backward/forward compatibility and rolling upgrades are
quite achievable. May your application’s evolution be rapid and your deployments be frequent. ##### Footnotes [i](ch04.html#idm140605777487312-marker) With the exception of some special
cases, such as certain memory-mapped files or when operating directly on compressed data (as described in
[“Column Compression”](ch03.html#sec_storage_column_compression)). [ii](ch04.html#idm140605777478016-marker) Note that encoding
has nothing to do with encryption. We don’t discuss encryption in this book. [iii](ch04.html#idm140605777137376-marker) Actually, it has three—BinaryProtocol,
CompactProtocol, and DenseProtocol—although DenseProtocol is only supported by the C++
implementation, so it doesn’t count as cross-language [[18](ch04.html#ThriftLangs)].
Besides those, it also has two different JSON-based encoding formats
[[19](ch04.html#Kleppmann2012tu)]. What fun!