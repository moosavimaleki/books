It seems that relational and document databases are becoming more similar over time, and that is a
good thing: the data models complement each
other.[v](ch02.html#idm140605782034240) If a database is able to handle document-like data and also perform
relational queries on it, applications can use the combination of features that best fits their
needs. A hybrid of the relational and document models is a good route for databases to take in the future. # Query Languages for Data 
When the relational model was introduced, it included a new way of querying data: SQL is a
declarative query language, whereas IMS and CODASYL queried the database using imperative code.
What does that mean? 
Many commonly used programming languages are imperative. For example, if you have a list of animal
species, you might write something like this to return only the sharks in the list: ```
`function` `getSharks``()` `{`
    `var` `sharks` `=` `[];`
    `for` `(``var` `i` `=` `0``;` `i` `<` `animals``.``length``;` `i``++``)` `{`
        `if` `(``animals``[``i``].``family` `===` `"Sharks"``)` `{`
            `sharks``.``push``(``animals``[``i``]);`
        `}`
    `}`
    `return` `sharks``;`
`}`
```