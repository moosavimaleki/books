URL `http://my-company.com/namespace#within` لزوماً نیازی به حل شدن به چیزی ندارد—از دیدگاه RDF، این فقط یک فضای نام است. برای جلوگیری از سردرگمی احتمالی با URLهای http://، مثال‌های این بخش از URIهای غیرقابل حل مانند urn:example:within استفاده می‌کنند. خوشبختانه، می‌توانید این پیشوند را فقط یک بار در بالای فایل مشخص کنید، و سپس آن را فراموش کنید.

### زبان پرس‌وجوی SPARQL

SPARQL یک زبان پرس‌وجو برای پایگاه‌های داده سه‌تایی است که از مدل داده RDF استفاده می‌کند [[43](ch02.html#Harris2013wd)]. (این یک مخفف برای SPARQL Protocol and RDF Query Language است، که "sparkle" تلفظ می‌شود.)

SPARQL قبل از Cypher وجود داشته است، و از آنجا که تطبیق الگوی Cypher از SPARQL گرفته شده است، آن‌ها بسیار شبیه به هم به نظر می‌رسند [[37](ch02.html#Neo4j2013)]. همان پرس‌وجوی قبلی—یافتن افرادی که از ایالات متحده به اروپا نقل مکان کرده‌اند—در SPARQL حتی مختصرتر از Cypher است (به [مثال 2-9](#fig_sparql_query) نگاه کنید).

##### مثال 2-9. همان پرس‌وجوی [مثال 2-4](#fig_cypher_query)، بیان شده در SPARQL

```
PREFIX : <urn:example:>

SELECT ?personName WHERE {
  ?person :name ?personName.
  ?person :bornIn  / :within* / :name "United States".
  ?person :livesIn / :within* / :name "Europe".
}