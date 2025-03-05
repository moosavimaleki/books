## The Cypher Query Language Cypher is a declarative query language for property graphs, created for the Neo4j graph database
[[37](ch02.html#Neo4j2013)]. (It is named after a character in the movie The Matrix
and is not related to ciphers in cryptography [[38](ch02.html#EifremTweet)].) [Example 2-3](#fig_cypher_create) shows the Cypher query to insert the lefthand portion of
[Figure 2-5](#fig_datamodels_graph) into a graph database. The rest of the graph can be added similarly and is
omitted for readability. Each vertex is given a symbolic name like USA or Idaho, and other parts
of the query can use those names to create edges between the vertices, using an arrow notation:
(Idaho) -[:WITHIN]-> (USA) creates an edge labeled WITHIN, with Idaho as the tail node and USA
as the head node. ##### Example 2-3. A subset of the data in [Figure 2-5](#fig_datamodels_graph), represented as a Cypher query ```
`CREATE```
`  (NAmerica:Location {name:``'North America'``, ``type``:``'continent'``}),`
`  (USA:Location      {name:``'United States'``, ``type``:``'country'``  }),`
`  (Idaho:Location    {name:``'Idaho'``,         ``type``:``'state'``    }),`
`  (Lucy:Person       {name:``'Lucy'`` }),`
`  (Idaho) -[:WITHIN]->  (USA)  -[:WITHIN]-> (NAmerica),`
`  (Lucy)  -[:BORN_IN]-> (Idaho)`
```