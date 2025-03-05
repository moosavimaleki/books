
There are two popular approaches to web services: REST and SOAP. They are almost diametrically
opposed in terms of philosophy, and often the subject of heated debate among their respective
proponents.[vi](ch04.html#idm140605776770048) 
REST is not a protocol, but rather a design philosophy that builds upon the principles of HTTP
[[34](ch04.html#Fielding2000vh), [35](ch04.html#Fielding2008wj)].
It emphasizes simple data formats, using URLs for identifying resources and using HTTP features for
cache control, authentication, and content type negotiation. REST has been gaining popularity
compared to SOAP, at least in the context of cross-organizational service integration
[[36](ch04.html#Pingdom2010)],
and is often associated with microservices
[[31](ch04.html#Newman2015wq)]. An API designed according to the
principles of REST is called RESTful. 
By contrast, SOAP is an XML-based protocol for making network API
requests.[vii](ch04.html#idm140605776754080)
Although it is most commonly used over HTTP, it aims to be independent from HTTP and avoids using
most HTTP features. Instead, it comes with a sprawling and complex multitude of related standards
(the web service framework, known as WS-*) that add various features
[[37](ch04.html#Innoq2007)].