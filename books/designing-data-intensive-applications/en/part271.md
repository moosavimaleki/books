
RESTful APIs tend to favor simpler approaches, typically involving less code generation and
automated tooling. A definition format such as OpenAPI, also known as Swagger
[[40](ch04.html#Swagger2014)], can be used to describe RESTful APIs and produce
documentation. ### The problems with remote procedure calls (RPCs) 
Web services are merely the latest incarnation of a long line of technologies for making API
requests over a network, many of which received a lot of hype but have serious problems. Enterprise
JavaBeans (EJB) and Java’s Remote Method Invocation (RMI) are limited to Java. The Distributed
Component Object Model (DCOM) is limited to Microsoft platforms. The Common Object Request Broker
Architecture (CORBA) is excessively complex, and does not provide backward or forward
compatibility [[41](ch04.html#Henning2006jb)]. 
All of these are based on the idea of a remote procedure call (RPC), which has been around since
the 1970s [[42](ch04.html#Birrell1984hv)].
The RPC model tries to make a request to a remote network service look the same as calling a function or
method in your programming language, within the same process (this abstraction is called location
transparency). Although RPC seems convenient at first, the approach is fundamentally flawed
[[43](ch04.html#Waldo1994wx_ch4),
[44](ch04.html#Vinoski2008gv)].
A network request is very different from a local function call: