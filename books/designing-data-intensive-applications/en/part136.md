One possible way of applying the rules is thus: 1.  name(namerica, 'North America') exists in the database, so rule 1
applies. It generates within_recursive(namerica, 'North America'). 2.  within(usa, namerica) exists in the database and the previous step generated
within_recursive(namerica, 'North America'), so rule 2 applies. It generates
within_recursive(usa, 'North America'). 3.  within(idaho, usa) exists in the database and the previous step generated
within_recursive(usa, 'North America'), so rule 2 applies. It generates
within_recursive(idaho, 'North America'). By repeated application of rules 1 and 2, the within_recursive predicate can tell us all the
locations in North America (or any other location name) contained in our database. This process is
illustrated in [Figure 2-6](#fig_datalog_naive). ![ddia 0206](assets/ddia_0206.png) ###### Figure 2-6. Determining that Idaho is in North America, using the Datalog rules from [Example 2-11](#fig_datalog_query). Now rule 3 can find people who were born in some location BornIn and live in some location
LivingIn. By querying with BornIn = 'United States' and
LivingIn = 'Europe', and leaving the person as a variable Who, we ask
the Datalog system to find out which values can appear for the variable Who.
So, finally we get the same answer as in the earlier Cypher and SPARQL queries.