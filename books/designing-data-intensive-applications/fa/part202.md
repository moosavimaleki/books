##### مثال 3-1. تحلیل اینکه آیا مردم بسته به روز هفته، بیشتر تمایل به خرید میوه تازه یا شیرینی دارند ```
`SELECT`
  `dim_date``.``weekday``,` `dim_product``.``category``,`
  `SUM``(``fact_sales``.``quantity``)` `AS` `quantity_sold`
`FROM` `fact_sales`
  `JOIN` `dim_date`    `ON` `fact_sales``.``date_key`   `=` `dim_date``.``date_key`
  `JOIN` `dim_product` `ON` `fact_sales``.``product_sk` `=` `dim_product``.``product_sk`
`WHERE`
  `dim_date``.``year` `=` `2013` `AND`
  `dim_product``.``category` `IN` `(``'Fresh fruit'``,` `'Candy'``)`
`GROUP` `BY`
  `dim_date``.``weekday``,` `dim_product``.``category``;`
``` 

چگونه می‌توانیم این پرس‌وجو را به طور کارآمد اجرا کنیم؟

در بیشتر پایگاه‌های داده OLTP، ذخیره‌سازی به صورت سطر-محور (row-oriented) چیده شده است: تمام مقادیر از یک سطر جدول در کنار یکدیگر ذخیره می‌شوند. پایگاه‌های داده سندی (Document databases) مشابه هستند: معمولاً یک سند کامل به عنوان یک توالی پیوسته از بایت‌ها ذخیره می‌شود. شما می‌توانید این را در مثال CSV [شکل 3-1](#fig_storage_csv_hash_index) ببینید. برای پردازش پرس‌وجویی مانند [مثال 3-1](#fig_storage_analytics_query)، ممکن است شاخص‌هایی (indexes) روی fact_sales.date_key و/یا fact_sales.product_sk داشته باشید که به موتور ذخیره‌سازی می‌گویند کجا تمام فروش‌ها برای یک تاریخ خاص یا برای یک محصول خاص را پیدا کند. اما سپس، یک موتور ذخیره‌سازی سطر-محور همچنان نیاز دارد تمام آن سطرها (هر کدام شامل بیش از 100 ویژگی) را از دیسک به حافظه بارگذاری کند، آن‌ها را تجزیه کند و آن‌هایی را که شرایط مورد نیاز را برآورده نمی‌کنند، فیلتر کند. این می‌تواند زمان زیادی طول بکشد.