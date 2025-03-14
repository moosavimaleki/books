هر دو Thrift و Protocol Buffers نیاز به یک طرح‌واره برای هر داده‌ای که کدگذاری می‌شود، دارند. برای کدگذاری داده
در [مثال 4-1](#fig_encoding_json) در Thrift، شما طرح‌واره را در زبان تعریف
رابط (IDL) Thrift به این صورت توصیف می‌کنید: ```
`struct` `Person` `{`
  `1``:` `required` `string`       `userName``,`
  `2``:` `optional` `i64`          `favoriteNumber``,`
  `3``:` `optional` `list``<``string``>` `interests`
`}`
``` 

تعریف طرح‌واره معادل برای Protocol Buffers بسیار مشابه به نظر می‌رسد: ```
`message` `Person` `{`
    `required` `string` `user_name`       `=` `1``;`
    `optional` `int64`  `favorite_number` `=` `2``;`
    `repeated` `string` `interests`       `=` `3``;`
`}`
``` 

Thrift و Protocol Buffers هر کدام با یک ابزار تولید کد همراه هستند که یک تعریف طرح‌واره
مانند آنچه در اینجا نشان داده شده است را می‌گیرد، و کلاس‌هایی تولید می‌کند که طرح‌واره را در زبان‌های برنامه‌نویسی مختلف
پیاده‌سازی می‌کنند [[18](ch04.html#ThriftLangs)]. کد برنامه شما می‌تواند این کد تولید شده را برای کدگذاری
یا رمزگشایی رکوردهای طرح‌واره فراخوانی کند.

داده‌های کدگذاری شده با این طرح‌واره چگونه به نظر می‌رسند؟ به طور گیج‌کننده‌ای، Thrift دو قالب کدگذاری باینری متفاوت
دارد،[iii](ch04.html#idm140605777137376)
که به ترتیب BinaryProtocol و CompactProtocol نامیده می‌شوند. بیایید ابتدا به BinaryProtocol نگاه کنیم.
کدگذاری [مثال 4-1](#fig_encoding_json) در آن قالب 59 بایت طول می‌کشد، همانطور که در
[شکل 4-2](#fig_encoding_thrift_binary) نشان داده شده است [[19](ch04.html#Kleppmann2012tu)].