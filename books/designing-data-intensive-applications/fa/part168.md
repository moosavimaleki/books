مانند SSTable‌ها، درخت‌های B جفت‌های کلید-مقدار را بر اساس کلید مرتب نگه می‌دارند، که اجازه می‌دهد جستجوی کلید-مقدار و پرس‌وجوهای محدوده به طور کارآمد انجام شوند. اما شباهت به همین‌جا ختم می‌شود: درخت‌های B فلسفه طراحی بسیار متفاوتی دارند.

شاخص‌های با ساختار لاگ که قبلاً دیدیم، پایگاه داده را به قطعات با اندازه متغیر تقسیم می‌کنند، معمولاً چندین مگابایت یا بیشتر در اندازه، و همیشه یک قطعه را به صورت متوالی می‌نویسند. در مقابل، درخت‌های B پایگاه داده را به بلوک‌ها یا صفحات با اندازه ثابت تقسیم می‌کنند، به طور سنتی 4 کیلوبایت در اندازه (گاهی بزرگتر)، و یک صفحه را در یک زمان می‌خوانند یا می‌نویسند. این طراحی بیشتر با سخت‌افزار زیربنایی مطابقت دارد، زیرا دیسک‌ها نیز در بلوک‌های با اندازه ثابت تنظیم شده‌اند.

هر صفحه می‌تواند با استفاده از یک آدرس یا مکان شناسایی شود، که اجازه می‌دهد یک صفحه به صفحه دیگر اشاره کند—مشابه یک اشاره‌گر، اما روی دیسک به جای در حافظه. می‌توانیم از این ارجاعات صفحه برای ساخت یک درخت از صفحات استفاده کنیم، همانطور که در [شکل 3-6](#fig_storage_b_tree) نشان داده شده است.

![ddia 0306](assets/ddia_0306.png)
###### شکل 3-6. جستجوی یک کلید با استفاده از یک شاخص درخت B. 