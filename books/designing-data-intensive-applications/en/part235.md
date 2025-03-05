This is a problem when dealing with large numbers; for example, integers greater than 253 cannot
be exactly represented in an IEEE 754 double-precision floating-point number, so such numbers become
inaccurate when parsed in a language that uses floating-point numbers (such as JavaScript). An
example of numbers larger than 253 occurs on Twitter, which uses a 64-bit number to identify each
tweet. The JSON returned by Twitter’s API includes tweet IDs twice, once as a JSON number and once
as a decimal string, to work around the fact that the numbers are not correctly parsed by JavaScript
applications [[10](ch04.html#Harris2010vu)]. *  
JSON and XML have good support for Unicode character strings (i.e., human-readable text), but they
don’t support binary strings (sequences of bytes without a character encoding). Binary strings are a
useful feature, so people get around this limitation by encoding the binary data as text using
Base64. The schema is then used to indicate that the value should be interpreted as Base64-encoded.
This works, but it’s somewhat hacky and increases the data size by 33%.