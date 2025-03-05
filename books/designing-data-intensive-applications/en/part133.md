*  In CODASYL, all queries were imperative, difficult to write and easily broken by changes in the
schema. In a graph database, you can write your traversal in imperative code if you want to, but
most graph databases also support high-level, declarative query languages such as Cypher or
SPARQL. ## The Foundation: Datalog Datalog is a much older language than SPARQL or Cypher, having been studied extensively by academics
in the 1980s
[[44](ch02.html#Green2013js),
[45](ch02.html#Ceri1989ff),
[46](ch02.html#Abiteboul1995ug)].
It is less well known among software engineers, but it is nevertheless important, because it
provides the foundation that later query languages build upon. 
In practice, Datalog is used in a few data systems: for example, it is the query language of Datomic
[[40](ch02.html#Datomic2013)], and Cascalog
[[47](ch02.html#MarzCascalog)]
is a Datalog implementation for querying large datasets in
Hadoop.[viii](ch02.html#idm140605780118640) Datalog’s data model is similar to the triple-store model, generalized a bit. Instead of writing a
triple as (subject, predicate, object), we write it as predicate(subject, object).
[Example 2-10](#fig_datalog_triples) shows how to write the data from our example in Datalog.