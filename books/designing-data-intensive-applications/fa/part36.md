* یک فرآیند خارج از کنترل که از برخی منابع مشترک استفاده می‌کند—زمان CPU، حافظه، فضای دیسک یا پهنای باند شبکه.

* یک سرویس که سیستم به آن وابسته است که کند می‌شود، غیرپاسخگو می‌شود، یا شروع به بازگرداندن پاسخ‌های خراب می‌کند.

* خرابی‌های آبشاری، جایی که یک خطای کوچک در یک مؤلفه باعث خطا در مؤلفه دیگر می‌شود، که به نوبه خود باعث خطاهای بیشتر می‌شود
[[10](ch01.html#AmazonWebServices2011tj)].

باگ‌هایی که باعث این نوع خطاهای نرم‌افزاری می‌شوند اغلب برای مدت طولانی خفته می‌مانند تا زمانی که توسط مجموعه‌ای از شرایط غیرعادی فعال شوند. در آن شرایط، مشخص می‌شود که نرم‌افزار فرضی درباره محیط خود می‌کند—و در حالی که آن فرض معمولاً درست است، نهایتاً به دلیلی درست بودن آن متوقف می‌شود
[[11](ch01.html#Cook2000wo)].

هیچ راه حل سریعی برای مشکل خطاهای سیستماتیک در نرم‌افزار وجود ندارد. چیزهای کوچک زیادی می‌توانند کمک کنند: تفکر دقیق درباره فرض‌ها و تعاملات در سیستم؛ آزمایش کامل؛ ایزوله کردن فرآیندها؛ اجازه دادن به فرآیندها برای فروپاشی و راه‌اندازی مجدد؛ اندازه‌گیری، نظارت و تحلیل رفتار سیستم در محیط تولید. اگر انتظار می‌رود یک سیستم تضمینی ارائه دهد (به عنوان مثال، در یک صف پیام، اینکه تعداد پیام‌های ورودی برابر با تعداد پیام‌های خروجی است)، می‌تواند به طور مداوم خود را در حین اجرا بررسی کند و در صورت یافتن مغایرت، هشدار دهد
[[12](ch01.html#Kreps2012td_ch1)]. 