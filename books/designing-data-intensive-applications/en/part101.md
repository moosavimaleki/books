
In the relational algebra, you would instead write: sharks  =  σfamily = “Sharks” (animals) where σ (the Greek letter sigma) is the selection operator, returning only those animals that
match the condition family = “Sharks”. 
When SQL was defined, it followed the structure of the relational algebra fairly closely: ```
`SELECT` `*` `FROM` `animals` `WHERE` `family` `=` `'Sharks'``;`
``` An imperative language tells the computer to perform certain operations in a certain order. You can
imagine stepping through the code line by line, evaluating conditions, updating variables, and
deciding whether to go around the loop one more time. In a declarative query language, like SQL or relational algebra, you just specify the pattern of the
data you want—what conditions the results must meet, and how you want the data to be transformed (e.g.,
sorted, grouped, and aggregated)—but not how to achieve that goal. It is up to the database
system’s query optimizer to decide which indexes and which join methods to use, and in which order
to execute various parts of the query.