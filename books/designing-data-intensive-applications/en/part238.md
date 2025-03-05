##### Example 4-1. Example record which we will encode in several binary formats in this chapter ```
`{`
    `"userName"``:` `"Martin"``,`
    `"favoriteNumber"``:` `1337``,`
    `"interests"``:` `[``"daydreaming"``,` `"hacking"``]`
`}`
``` 
Let’s look at an example of MessagePack, a binary encoding for JSON. [Figure 4-1](#fig_encoding_messagepack)
shows the byte sequence that you get if you encode the JSON document in [Example 4-1](#fig_encoding_json) with
MessagePack [[14](ch04.html#MsgPack)]. The first few bytes are as follows: 1.  The first byte, 0x83, indicates that what follows is an object (top four bits = 0x80) with three
fields (bottom four bits = 0x03). (In case you’re wondering what happens if an object has more
than 15 fields, so that the number of fields doesn’t fit in four bits, it then gets a different type
indicator, and the number of fields is encoded in two or four bytes.) 2.  The second byte, 0xa8, indicates that what follows is a string (top four bits = 0xa0) that is eight
bytes long (bottom four bits = 0x08).