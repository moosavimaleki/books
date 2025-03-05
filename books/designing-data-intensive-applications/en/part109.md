[![2](assets/2.png)](#co_data_models_and_query_languages_CO3-1) The JavaScript function map is called once for every document that matches query, with
this set to the document object. [![3](assets/3.png)](#co_data_models_and_query_languages_CO3-2) The map function emits a key (a string consisting of year and month, such as "2013-12" or
"2014-1") and a value (the number of animals in that observation). [![4](assets/4.png)](#co_data_models_and_query_languages_CO3-3) The key-value pairs emitted by map are grouped by key. For all key-value pairs with the same
key (i.e., the same month and year), the reduce function is called once. [![5](assets/5.png)](#co_data_models_and_query_languages_CO3-4) The reduce function adds up the number of animals from all observations in a particular month. [![6](assets/6.png)](#co_data_models_and_query_languages_CO3-6) The final output is written to the collection monthlySharkReport. For example, say the observations collection contains these two documents: ```
`{`
    `observationTimestamp``:` `Date``.``parse``(``"Mon, 25 Dec 1995 12:34:56 GMT"``),`
    `family``:`     `"Sharks"``,`
    `species``:`    `"Carcharodon carcharias"``,`
    `numAnimals``:` `3`
`}`
`{`
    `observationTimestamp``:` `Date``.``parse``(``"Tue, 12 Dec 1995 16:17:18 GMT"``),`
    `family``:`     `"Sharks"``,`
    `species``:`    `"Carcharias taurus"``,`
    `numAnimals``:` `4`
`}`
```