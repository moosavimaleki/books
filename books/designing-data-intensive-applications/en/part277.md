*  
In SOAP, requests and responses are specified with XML schemas. These can be evolved, but there
are some subtle pitfalls
[[47](ch04.html#Narayan2007vg)]. *  RESTful APIs most commonly use JSON (without a formally specified schema) for responses, and
JSON or URI-encoded/form-encoded request parameters for requests. Adding optional request
parameters and adding new fields to response objects are usually considered changes that maintain
compatibility. Service compatibility is made harder by the fact that RPC is often used for communication across
organizational boundaries, so the provider of a service often has no control over its clients and
cannot force them to upgrade. Thus, compatibility needs to be maintained for a long time, perhaps
indefinitely. If a compatibility-breaking change is required, the service provider often ends up
maintaining multiple versions of the service API side by side. There is no agreement on how API versioning should work (i.e., how a client can indicate which
version of the API it wants to use [[48](ch04.html#Hunt2014wn)]). For RESTful APIs, common approaches are to use a version
number in the URL or in the HTTP Accept header. For services that use API keys to identify a
particular client, another option is to store a client’s requested API version on the server and to
allow this version selection to be updated through a separate administrative interface
[[49](ch04.html#StripeAPI)].