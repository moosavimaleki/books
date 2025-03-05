*   There is optional schema support for both XML
[[11](ch04.html#W3CXMLSchema)] and JSON
[[12](ch04.html#Galiegue2013wu)].
These schema languages are quite powerful, and thus quite complicated to learn and implement. Use of
XML schemas is fairly widespread, but many JSON-based tools don’t bother using schemas. Since the
correct interpretation of data (such as numbers and binary strings) depends on information in the
schema, applications that don’t use XML/JSON schemas need to potentially hardcode the appropriate
encoding/decoding logic instead. *  CSV does not have any schema, so it is up to the application to define the meaning of each row and
column. If an application change adds a new row or column, you have to handle that change manually.
CSV is also a quite vague format (what happens if a value contains a comma or a newline character?).
Although its escaping rules have been formally specified
[[13](ch04.html#Shafranovich2005vq)],
not all parsers implement them correctly. Despite these flaws, JSON, XML, and CSV are good enough for many purposes. It’s likely that they will
remain popular, especially as data interchange formats (i.e., for sending data from one organization to
another). In these situations, as long as people agree on what the format is, it often doesn’t
matter how pretty or efficient the format is. The difficulty of getting different organizations to
agree on anything outweighs most other concerns.