
Web browsers are not the only type of client. For example, a native app running on a mobile device
or a desktop computer can also make network requests to a server, and a client-side JavaScript
application running inside a web browser can use XMLHttpRequest to become an HTTP client (this
technique is known as Ajax [[30](ch04.html#Garrett2005wi)]).
In this case, the server’s response is typically not HTML for displaying to a human, but rather data
in an encoding that is convenient for further processing by the client-side application code (such
as JSON). Although HTTP may be used as the transport protocol, the API implemented on top is
application-specific, and the client and server need to agree on the details of that API. 
Moreover, a server can itself be a client to another service (for example, a typical web app server
acts as client to a database). This approach is often used to decompose a large application into
smaller services by area of functionality, such that one service makes a request to another when it
requires some functionality or data from that other service. This way of building applications has
traditionally been called a service-oriented architecture (SOA), more recently refined and
rebranded as microservices architecture
[[31](ch04.html#Newman2015wq),
[32](ch04.html#Richardson2014wv)].