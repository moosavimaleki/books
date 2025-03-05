[![1](assets/1.png)](#co_data_models_and_query_languages_CO2-1) تابع `date_trunc('month', timestamp)` ماه تقویمی شامل timestamp را تعیین می‌کند و timestamp دیگری را برمی‌گرداند که نشان‌دهنده ابتدای آن ماه است. به عبارت دیگر، یک timestamp را به نزدیک‌ترین ماه گرد می‌کند.

این پرس‌وجو ابتدا مشاهدات را فیلتر می‌کند تا فقط گونه‌های خانواده کوسه‌ها را نشان دهد، سپس مشاهدات را بر اساس ماه تقویمی که در آن رخ داده‌اند گروه‌بندی می‌کند، و در نهایت تعداد حیوانات دیده شده در تمام مشاهدات در آن ماه را جمع می‌زند.

همین مورد را می‌توان با ویژگی MapReduce مونگودی‌بی به شرح زیر بیان کرد:
```
db.observations.mapReduce(
    function map() { [![2](assets/2.png)](#callout_data_models_and_query_languages_CO3-2)
        var year  = this.observationTimestamp.getFullYear();
        var month = this.observationTimestamp.getMonth() + 1;
        emit(year + "-" + month, this.numAnimals); [![3](assets/3.png)](#callout_data_models_and_query_languages_CO3-3)
    },
    function reduce(key, values) { [![4](assets/4.png)](#callout_data_models_and_query_languages_CO3-4)
        return Array.sum(values); [![5](assets/5.png)](#callout_data_models_and_query_languages_CO3-5)
    },
    {
        query: { family: "Sharks" }, [![1](assets/1.png)](#callout_data_models_and_query_languages_CO3-1)
        out: "monthlySharkReport" [![6](assets/6.png)](#callout_data_models_and_query_languages_CO3-6)
    }
);
```

[![1](assets/1.png)](#co_data_models_and_query_languages_CO3-5) فیلتر برای در نظر گرفتن فقط گونه‌های کوسه می‌تواند به صورت اعلانی مشخص شود (این یک افزونه مخصوص مونگودی‌بی به MapReduce است).% 