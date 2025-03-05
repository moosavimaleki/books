
In this section we will use the example shown in [Figure 2-5](#fig_datamodels_graph). It could be taken from a
social network or a genealogical database: it shows two people, Lucy from Idaho and Alain from
Beaune, France. They are married and living in London. ![ddia 0205](assets/ddia_0205.png) ###### Figure 2-5. Example of graph-structured data (boxes represent vertices, arrows represent edges). 
There are several different, but related, ways of structuring and querying data in graphs. In this
section we will discuss the property graph model (implemented by Neo4j, Titan, and InfiniteGraph) and
the triple-store model (implemented by Datomic, AllegroGraph, and others). We will look at three
declarative query languages for graphs: Cypher, SPARQL, and Datalog. Besides these, there are also
imperative graph query languages such as Gremlin
[[36](ch02.html#Gremlin2013)]
and graph processing frameworks like Pregel (see [Chapter 10](ch10.html#ch_batch)). ## Property Graphs 
In the property graph model, each vertex consists of: *  A unique identifier