## زبان پرس‌وجوی Cypher

Cypher یک زبان پرس‌وجوی اعلانی برای گراف‌های ویژگی است که برای پایگاه داده گراف Neo4j ایجاد شده است [[37](ch02.html#Neo4j2013)]. (این زبان به نام یک شخصیت در فیلم ماتریکس نامگذاری شده است و ارتباطی با رمزها در رمزنگاری ندارد [[38](ch02.html#EifremTweet)].) [مثال 2-3](#fig_cypher_create) پرس‌وجوی Cypher برای درج بخش سمت چپ [شکل 2-5](#fig_datamodels_graph) در یک پایگاه داده گراف را نشان می‌دهد. بقیه گراف می‌تواند به طور مشابه اضافه شود و برای خوانایی حذف شده است.

به هر رأس یک نام نمادین مانند USA یا Idaho داده می‌شود، و بخش‌های دیگر پرس‌وجو می‌توانند از آن نام‌ها برای ایجاد یال‌ها بین رئوس، با استفاده از نماد فلش استفاده کنند: (Idaho) -[:WITHIN]-> (USA) یک یال با برچسب WITHIN ایجاد می‌کند، با Idaho به عنوان گره دم و USA به عنوان گره سر.

##### مثال 2-3. زیرمجموعه‌ای از داده‌های [شکل 2-5](#fig_datamodels_graph)، نمایش داده شده به عنوان یک پرس‌وجوی Cypher

```
CREATE
  (NAmerica:Location {name:'North America', type:'continent'}),
  (USA:Location      {name:'United States', type:'country'  }),
  (Idaho:Location    {name:'Idaho',         type:'state'    }),
  (Lucy:Person       {name:'Lucy' }),
  (Idaho) -[:WITHIN]->  (USA)  -[:WITHIN]-> (NAmerica),
  (Lucy)  -[:BORN_IN]-> (Idaho)
```% 