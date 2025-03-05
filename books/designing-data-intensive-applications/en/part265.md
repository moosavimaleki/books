In [Chapter 10](ch10.html#ch_batch) we will talk more about using data in archival storage. ## Dataflow Through Services: REST and RPC 
When you have processes that need to communicate over a network, there are a few different ways of
arranging that communication. The most common arrangement is to have two roles: clients and
servers. The servers expose an API over the network, and the clients can connect to the servers
to make requests to that API. The API exposed by the server is known as a service. The web works this way: clients (web browsers) make requests to web servers, making GET requests
to download HTML, CSS, JavaScript, images, etc., and making POST requests to submit data to the
server. The API consists of a standardized set of protocols and data formats (HTTP, URLs, SSL/TLS,
HTML, etc.). Because web browsers, web servers, and website authors mostly agree on these standards,
you can use any web browser to access any website (at least in theory!).