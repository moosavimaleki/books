* برای پاسخ به یک درخواست خواندن، ابتدا سعی کنید کلید را در memtable پیدا کنید، سپس در جدیدترین قطعه روی دیسک، سپس در قطعه قدیمی‌تر بعدی، و غیره.

* هر از گاهی، یک فرآیند ادغام و فشرده‌سازی را در پس‌زمینه اجرا کنید تا فایل‌های قطعه را ترکیب کند و مقادیر بازنویسی شده یا حذف شده را دور بیندازد.

این طرح بسیار خوب کار می‌کند. فقط از یک مشکل رنج می‌برد: اگر پایگاه داده خراب شود، جدیدترین نوشتن‌ها (که در memtable هستند اما هنوز به دیسک نوشته نشده‌اند) از دست می‌روند. برای جلوگیری از آن مشکل، می‌توانیم یک لاگ جداگانه روی دیسک نگه داریم که هر نوشتن بلافاصله به آن اضافه می‌شود، درست مانند بخش قبلی. آن لاگ به ترتیب مرتب شده نیست، اما این مهم نیست، زیرا تنها هدف آن بازیابی memtable پس از یک خرابی است. هر بار که memtable به یک SSTable نوشته می‌شود، لاگ مربوطه می‌تواند دور انداخته شود. 