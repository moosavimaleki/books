
This new generation of RPC frameworks is more explicit about the fact that a remote request is
different from a local function call. For example, Finagle and Rest.li use futures (promises) to
encapsulate asynchronous actions that may fail. Futures also simplify situations where you need to
make requests to multiple services in parallel, and combine their results
[[45](ch04.html#Eriksen2013gz)].
gRPC supports streams, where a call consists of not just one request and one response, but a
series of requests and responses over time
[[46](ch04.html#gRPC2015)]. 
Some of these frameworks also provide service discovery—that is, allowing a client to find out
at which IP address and port number it can find a particular service. We will return to this topic
in [“Request Routing”](ch06.html#sec_partitioning_routing). 
Custom RPC protocols with a binary encoding format can achieve better performance than something
generic like JSON over REST. However, a RESTful API has other significant advantages: it is good for
experimentation and debugging (you can simply make requests to it using a web browser or the
command-line tool curl, without any code generation or software installation), it is supported by
all mainstream programming languages and platforms, and there is a vast ecosystem of tools available (servers,
caches, load balancers, proxies, firewalls, monitoring, debugging tools, testing tools, etc.).