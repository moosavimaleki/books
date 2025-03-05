```
`MATCH```
`  (person) -[:BORN_IN]->  () -[:WITHIN*0..]-> (us:Location {name:``'United States'``}),`
`  (person) -[:LIVES_IN]-> () -[:WITHIN*0..]-> (eu:Location {name:``'Europe'``})`
`RETURN ``person.name`
``` The query can be read as follows: Find any vertex (call it person) that meets both of the
following conditions: 1.  person has an outgoing BORN_IN edge to some vertex. From that vertex, you can follow a chain
of outgoing WITHIN edges until eventually you reach a vertex of type Location, whose name
property is equal to "United States". 2.  That same person vertex also has an outgoing LIVES_IN edge. Following that edge, and then a
chain of outgoing WITHIN edges, you eventually reach a vertex of type Location, whose name
property is equal to "Europe". For each such person vertex, return the name property. There are several possible ways of executing the query. The description given here suggests that you
start by scanning all the people in the database, examine each person’s birthplace and residence,
and return only those people who meet the criteria.