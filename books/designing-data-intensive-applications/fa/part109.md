[![2](assets/2.png)](#co_data_models_and_query_languages_CO3-1) تابع جاوااسکریپت map یک بار برای هر سندی که با query مطابقت دارد فراخوانی می‌شود، با this که به شیء سند تنظیم شده است.

[![3](assets/3.png)](#co_data_models_and_query_languages_CO3-2) تابع map یک کلید (یک رشته متشکل از سال و ماه، مانند "2013-12" یا "2014-1") و یک مقدار (تعداد حیوانات در آن مشاهده) را منتشر می‌کند.

[![4](assets/4.png)](#co_data_models_and_query_languages_CO3-3) جفت‌های کلید-مقدار منتشر شده توسط map بر اساس کلید گروه‌بندی می‌شوند. برای تمام جفت‌های کلید-مقدار با کلید یکسان (یعنی، همان ماه و سال)، تابع reduce یک بار فراخوانی می‌شود.

[![5](assets/5.png)](#co_data_models_and_query_languages_CO3-4) تابع reduce تعداد حیوانات از تمام مشاهدات در یک ماه خاص را جمع می‌زند.

[![6](assets/6.png)](#co_data_models_and_query_languages_CO3-6) خروجی نهایی به مجموعه monthlySharkReport نوشته می‌شود.

به عنوان مثال، فرض کنید مجموعه observations شامل این دو سند است:
```
{
    observationTimestamp: Date.parse("Mon, 25 Dec 1995 12:34:56 GMT"),
    family:     "Sharks",
    species:    "Carcharodon carcharias",
    numAnimals: 3
}
{
    observationTimestamp: Date.parse("Tue, 12 Dec 1995 16:17:18 GMT"),
    family:     "Sharks",
    species:    "Carcharias taurus",
    numAnimals: 4
}
```% 