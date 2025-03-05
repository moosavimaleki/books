2. یک رأس دیگر در گراف. در این حالت، گزاره یک یال در گراف است، موضوع رأس دم است، و شیء رأس سر است. برای مثال، در (lucy, marriedTo, alain) موضوع و شیء lucy و alain هر دو رأس هستند، و گزاره marriedTo برچسب یالی است که آن‌ها را به هم متصل می‌کند.

[مثال 2-6](#fig_graph_n3_triples) همان داده‌های [مثال 2-3](#fig_cypher_create) را نشان می‌دهد، که به صورت سه‌تایی‌ها در قالبی به نام Turtle، زیرمجموعه‌ای از Notation3 (N3) [[39](ch02.html#Beckett2011vq)] نوشته شده است.

##### مثال 2-6. زیرمجموعه‌ای از داده‌های [شکل 2-5](#fig_datamodels_graph)، نمایش داده شده به صورت سه‌تایی‌های Turtle

```
@prefix : .
_:lucy     a       :Person.
_:lucy     :name   "Lucy".
_:lucy     :bornIn _:idaho.
_:idaho    a       :Location.
_:idaho    :name   "Idaho".
_:idaho    :type   "state".
_:idaho    :within _:usa.
_:usa      a       :Location.
_:usa      :name   "United States".
_:usa      :type   "country".
_:usa      :within _:namerica.
_:namerica a       :Location.
_:namerica :name   "North America".
_:namerica :type   "continent".
```

در این مثال، رأس‌های گراف به صورت _:someName نوشته شده‌اند. این نام خارج از این فایل معنایی ندارد؛ فقط به این دلیل وجود دارد که در غیر این صورت نمی‌دانستیم کدام سه‌تایی‌ها به یک رأس یکسان اشاره می‌کنند. وقتی گزاره یک یال را نشان می‌دهد، شیء یک رأس است، مانند _:idaho :within _:usa. وقتی گزاره یک ویژگی است، شیء یک رشته متنی است، مانند _:usa :name "United States". 