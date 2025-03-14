یک روش ممکن برای اعمال قوانین به این صورت است:

1. name(namerica, 'North America') در پایگاه داده وجود دارد، بنابراین قانون 1 اعمال می‌شود. این within_recursive(namerica, 'North America') را تولید می‌کند.

2. within(usa, namerica) در پایگاه داده وجود دارد و مرحله قبلی within_recursive(namerica, 'North America') را تولید کرده است، بنابراین قانون 2 اعمال می‌شود. این within_recursive(usa, 'North America') را تولید می‌کند.

3. within(idaho, usa) در پایگاه داده وجود دارد و مرحله قبلی within_recursive(usa, 'North America') را تولید کرده است، بنابراین قانون 2 اعمال می‌شود. این within_recursive(idaho, 'North America') را تولید می‌کند.

با اعمال مکرر قوانین 1 و 2، گزاره within_recursive می‌تواند تمام مکان‌های موجود در آمریکای شمالی (یا هر نام مکان دیگری) که در پایگاه داده ما وجود دارند را به ما بگوید. این فرآیند در [شکل 2-6](#fig_datalog_naive) نشان داده شده است.

![ddia 0206](assets/ddia_0206.png)

###### شکل 2-6. تعیین اینکه آیداهو در آمریکای شمالی است، با استفاده از قوانین Datalog از [مثال 2-11](#fig_datalog_query).

اکنون قانون 3 می‌تواند افرادی را پیدا کند که در مکانی BornIn متولد شده‌اند و در مکانی LivingIn زندگی می‌کنند. با پرس‌وجو با BornIn = 'United States' و LivingIn = 'Europe'، و با باقی گذاشتن شخص به عنوان متغیر Who، ما از سیستم Datalog می‌خواهیم که مشخص کند کدام مقادیر می‌توانند برای متغیر Who ظاهر شوند.

بنابراین، در نهایت ما همان پاسخی را که در پرس‌وجوهای قبلی Cypher و SPARQL داشتیم، به دست می‌آوریم.