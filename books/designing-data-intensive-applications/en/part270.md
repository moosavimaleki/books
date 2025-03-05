
The API of a SOAP web service is described using an XML-based language called the Web Services
Description Language, or WSDL. WSDL enables code generation so that a client can access a remote
service using local classes and method calls (which are encoded to XML messages and decoded again by
the framework). This is useful in statically typed programming languages, but less so in dynamically
typed ones (see [“Code generation and dynamically typed languages”](#sec_encoding_code_generation)). As WSDL is not designed to be human-readable, and as SOAP messages are often too complex to
construct manually, users of SOAP rely heavily on tool support, code generation, and IDEs
[[38](ch04.html#Lacey2006ul)].
For users of programming languages that are not supported by SOAP vendors, integration with SOAP
services is difficult. Even though SOAP and its various extensions are ostensibly standardized, interoperability between
different vendors’ implementations often causes problems
[[39](ch04.html#Tilkov2006tb)]. For all of these reasons,
although SOAP is still used in many large enterprises, it has fallen out of favor in most smaller
companies.