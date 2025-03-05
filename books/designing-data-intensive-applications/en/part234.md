## JSON, XML, and Binary Variants 
Moving to standardized encodings that can be written and read by many programming languages, JSON
and XML are the obvious contenders. They are widely known, widely supported, and almost as widely
disliked. XML is often criticized for being too verbose and unnecessarily complicated
[[9](ch04.html#XMLSExp)]. JSON’s popularity is mainly due to its
built-in support in web browsers (by virtue of being a subset of JavaScript) and simplicity relative
to XML. CSV is another popular language-independent format, albeit less powerful. JSON, XML, and CSV are textual formats, and thus somewhat human-readable (although the syntax is a
popular topic of debate). Besides the superficial syntactic issues, they also have some subtle
problems: *  
There is a lot of ambiguity around the encoding of numbers. In XML and CSV, you cannot distinguish
between a number and a string that happens to consist of digits (except by referring to an external
schema). JSON distinguishes strings and numbers, but it doesn’t distinguish integers and
floating-point numbers, and it doesn’t specify a precision.