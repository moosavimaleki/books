MapReduce به طور کلی در [فصل 10](ch10.html#ch_batch) با جزئیات بیشتری توصیف شده است. فعلاً، ما فقط به طور مختصر استفاده MongoDB از این مدل را بررسی می‌کنیم.

MapReduce نه یک زبان پرس‌وجوی اعلانی است و نه یک API پرس‌وجوی کاملاً دستوری، بلکه چیزی بین این دو است: منطق پرس‌وجو با قطعات کد بیان می‌شود که به طور مکرر توسط چارچوب پردازش فراخوانی می‌شوند. این بر اساس توابع map (همچنین به عنوان collect شناخته می‌شود) و reduce (همچنین به عنوان fold یا inject شناخته می‌شود) است که در بسیاری از زبان‌های برنامه‌نویسی تابعی وجود دارند.

برای ارائه یک مثال، تصور کنید شما یک زیست‌شناس دریایی هستید و هر بار که حیوانات را در اقیانوس می‌بینید، یک رکورد مشاهده به پایگاه داده خود اضافه می‌کنید. اکنون می‌خواهید گزارشی تهیه کنید که نشان دهد چند کوسه در هر ماه مشاهده کرده‌اید. در PostgreSQL ممکن است آن پرس‌وجو را به این صورت بیان کنید:
```
SELECT date_trunc('month', observation_timestamp) AS observation_month, [![1](assets/1.png)](#callout_data_models_and_query_languages_CO2-1)
       sum(num_animals) AS total_animals
FROM observations
WHERE family = 'Sharks'
GROUP BY observation_month;
```% 