##### Example 2-10. A subset of the data in [Figure 2-5](#fig_datamodels_graph), represented as Datalog facts ```
`name``(``namerica``,` `'North America'``).`
`type``(``namerica``,` `continent``).`

`name``(``usa``,` `'United States'``).`
`type``(``usa``,` `country``).`
`within``(``usa``,` `namerica``).`

`name``(``idaho``,` `'Idaho'``).`
`type``(``idaho``,` `state``).`
`within``(``idaho``,` `usa``).`

`name``(``lucy``,` `'Lucy'``).`
`born_in``(``lucy``,` `idaho``).`
``` 
Now that we have defined the data, we can write the same query as before, as shown in
[Example 2-11](#fig_datalog_query). It looks a bit different from the equivalent in Cypher or SPARQL, but don’t
let that put you off. Datalog is a subset of Prolog, which you might have seen before if you’ve
studied computer science. ##### Example 2-11. The same query as [Example 2-4](#fig_cypher_query), expressed in Datalog ```
`within_recursive``(``Location``,` `Name``)` `:-` `name``(``Location``,` `Name``).`     `/* Rule 1 */`

`within_recursive``(``Location``,` `Name``)` `:-` `within``(``Location``,` `Via``),`    `/* Rule 2 */`
                                    `within_recursive``(``Via``,` `Name``).`

`migrated``(``Name``,` `BornIn``,` `LivingIn``)` `:-` `name``(``Person``,` `Name``),`       `/* Rule 3 */`
                                    `born_in``(``Person``,` `BornLoc``),`
                                    `within_recursive``(``BornLoc``,` `BornIn``),`
                                    `lives_in``(``Person``,` `LivingLoc``),`
                                    `within_recursive``(``LivingLoc``,` `LivingIn``).`

`?-` `migrated``(``Who``,` `'United States'``,` `'Europe'``).`
`/* Who = 'Lucy'. */`
```