```
`{`
    `"type"``:` `"record"``,`
    `"name"``:` `"Person"``,`
    `"fields"``:` `[`
        `{``"name"``:` `"userName"``,`       `"type"``:` `"string"``},`
        `{``"name"``:` `"favoriteNumber"``,` `"type"``:` `[``"null"``,` `"long"``],` `"default"``:` `null``},`
        `{``"name"``:` `"interests"``,`      `"type"``:` `{``"type"``:` `"array"``,` `"items"``:` `"string"``}}`
    `]`
`}`
``` First of all, notice that there are no tag numbers in the schema. If we encode our example record
([Example 4-1](#fig_encoding_json)) using this schema, the Avro binary encoding is just 32 bytes long—the
most compact of all the encodings we have seen. The breakdown of the encoded byte sequence is shown
in [Figure 4-5](#fig_encoding_avro). 
If you examine the byte sequence, you can see that there is nothing to identify fields or their
datatypes. The encoding simply consists of values concatenated together. A string is just a length
prefix followed by UTF-8 bytes, but there’s nothing in the encoded data that tells you that it is a
string. It could just as well be an integer, or something else entirely. An integer is encoded using
a variable-length encoding (the same as Thrift’s CompactProtocol).