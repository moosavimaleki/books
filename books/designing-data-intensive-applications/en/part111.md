
Being able to use JavaScript code in the middle of a query is a great feature for advanced queries,
but it’s not limited to MapReduce—some SQL databases can be extended with JavaScript functions
too [[34](ch02.html#Kerstiens2013ur)]. 
A usability problem with MapReduce is that you have to write two carefully coordinated JavaScript
functions, which is often harder than writing a single query. Moreover, a declarative query language
offers more opportunities for a query optimizer to improve the performance of a query. For these
reasons, MongoDB 2.2 added support for a declarative query language called the aggregation pipeline
[[9](ch02.html#MongoDB2013)]. In this language, the same shark-counting
query looks like this: ```
`db``.``observations``.``aggregate``([`
    `{` `$match``:` `{` `family``:` `"Sharks"` `}` `},`
    `{` `$group``:` `{`
        `_id``:` `{`
            `year``:`  `{` `$year``:`  `"$observationTimestamp"` `},`
            `month``:` `{` `$month``:` `"$observationTimestamp"` `}`
        `},`
        `totalAnimals``:` `{` `$sum``:` `"$numAnimals"` `}`
    `}` `}`
`]);`
``` The aggregation pipeline language is similar in expressiveness to a subset of SQL, but it uses a
JSON-based syntax rather than SQL’s English-sentence-style syntax; the difference is perhaps a
matter of taste. The moral of the story is that a NoSQL system may find itself accidentally
reinventing SQL, albeit in disguise.