### Binary encoding 
For data that is used only internally within your organization, there is less pressure to use a
lowest-common-denominator encoding format. For example, you could choose a format that is more
compact or faster to parse. For a small dataset, the gains are negligible, but once you get into the
terabytes, the choice of data format can have a big impact. 
JSON is less verbose than XML, but both still use a lot of space compared to binary formats. This
observation led to the development of a profusion of binary encodings for JSON (MessagePack, BSON,
BJSON, UBJSON, BISON, and Smile, to name a few) and for XML (WBXML and Fast Infoset, for example).
These formats have been adopted in various niches, but none of them are as widely adopted as the
textual versions of JSON and XML. Some of these formats extend the set of datatypes (e.g., distinguishing integers and floating-point numbers,
or adding support for binary strings), but otherwise they keep the JSON/XML data model unchanged. In
particular, since they don’t prescribe a schema, they need to include all the object field names within
the encoded data. That is, in a binary encoding of the JSON document in [Example 4-1](#fig_encoding_json), they
will need to include the strings userName, favoriteNumber, and interests somewhere.